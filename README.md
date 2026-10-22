# Constrular — Sistema de Gestão para Loja de Material de Construção

![Testes](https://github.com/SEU_USUARIO/SEU_REPOSITORIO/actions/workflows/tests.yml/badge.svg)

Sistema de linha de comando (CLI) em Python para gestão de uma loja de
materiais de construção: cadastro de produtos, clientes, fornecedores
e funcionários, controle de estoque, registro de vendas e relatórios
gerenciais. Os dados são persistidos em um banco MySQL.

Projeto acadêmico desenvolvido com arquitetura em camadas
(config → models → repositories → services → menu), pensado também
como base de dados para análises em **Power BI**.

## Arquitetura

```
src/
├── config/         # Conexão com o banco (variáveis de ambiente)
├── models/         # Dataclasses que representam as entidades do domínio
├── repositories/    # Acesso direto ao banco (SQL puro)
├── services/        # Regras de negócio e validações
├── queries/          # Consultas analíticas (pandas) para exportação/Power BI
└── main.py          # Menu interativo (camada de apresentação)

scripts/
└── popular_banco.py # Gera dados mockados (12 meses de histórico)

database/
└── constrular.sql   # Schema completo + views + 5 registros de exemplo

tests/                # Testes automatizados (pytest) + scripts de
                       # demonstração manual das funcionalidades
```

Fluxo de dependência: `main.py` → `services` → `repositories` → `config`.
Cada camada só conhece a camada imediatamente abaixo dela, o que facilita
manutenção e testes.

## Pré-requisitos

- Python 3.11+
- MySQL Server 8.0+ (local ou remoto)

## Configuração

1. Clone o repositório e crie um ambiente virtual:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # Windows
   source .venv/bin/activate  # Linux/Mac
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Copie `.env.example` para `.env` e preencha com as credenciais do
   seu banco local:

   ```bash
   cp .env.example .env
   ```

   > ⚠️ **Nunca** faça commit do arquivo `.env` com a senha real —
   > ele já está no `.gitignore`.

4. Crie o schema e os dados de exemplo executando o script SQL:

   ```bash
   mysql -u root -p < database/constrular.sql
   ```

   Isso cria o banco `constrular` com todas as tabelas, views e um
   pequeno conjunto de dados de exemplo (5 registros por tabela).

## Como executar o sistema

A partir da raiz do projeto (para que os imports `src.*` funcionem):

```bash
python -m src.main
```

Isso abre o menu interativo no terminal com as opções de Produtos,
Clientes, Fornecedores, Funcionários, Vendas, Estoque e Relatórios.

## Gerando dados mockados para o Power BI

O dump SQL original traz apenas 5 registros por tabela — suficiente
para testar o sistema, mas insuficiente para gráficos de tendência,
sazonalidade ou ranking em um dashboard. Para isso, existe o script:

```bash
python -m scripts.popular_banco
```

Ele **adiciona** (sem apagar nada) ao banco já existente:

- 12 meses de histórico de vendas, com sazonalidade simples
  (mais vendas em novembro/dezembro, menos em fevereiro);
- ~75 clientes distribuídos em cidades do Vale do Paraíba;
- 30 produtos novos distribuídos nas 5 categorias já existentes;
- 5 fornecedores novos;
- 7 funcionários novos com salários variados por cargo;
- centenas de vendas com itens e preços variando ±5% (simulando
  negociação/promoções);
- movimentações de estoque (entradas e saídas) consistentes, sem
  nunca deixar o estoque simulado ficar negativo.

O script pede confirmação antes de rodar, e desfaz tudo automaticamente
(`ROLLBACK`) caso algum erro ocorra no meio do processo.

## Exportando relatórios para o Power BI

Além dos relatórios simples do menu (`src/services/relatorio_service.py`),
o projeto tem um módulo de relatórios analíticos que devolve os dados
como `pandas.DataFrame`, prontos para virar CSV:

```bash
python -m src.queries.relatorios
```

Isso gera uma pasta `relatorios_exportados/` na raiz do projeto com um
CSV para cada relatório:

| Arquivo                          | Conteúdo                                             |
|-----------------------------------|-------------------------------------------------------|
| `faturamento_mensal.csv`          | Faturamento, custo e lucro por mês                     |
| `faturamento_por_categoria.csv`   | Faturamento e lucro por categoria de produto           |
| `vendas_por_cidade.csv`           | Faturamento por cidade do cliente                      |
| `ticket_medio_mensal.csv`         | Ticket médio por mês                                   |
| `desempenho_funcionarios.csv`     | Vendas, faturamento e ticket médio por funcionário     |
| `top_clientes.csv`                | Ranking dos clientes que mais compraram                |
| `ranking_margem_produtos.csv`     | Margem de lucro por produto                             |
| `formas_pagamento_mensal.csv`     | Distribuição de faturamento por forma de pagamento     |
| `situacao_estoque.csv`            | Estoque atual, status e valor de custo parado          |
| `folha_pagamento_por_cargo.csv`   | Total de salários e headcount por cargo                |

No Power BI Desktop: **Obter Dados > Texto/CSV**, selecione os arquivos
desejados e monte suas visualizações. Alternativamente, é possível
conectar o Power BI diretamente ao MySQL (**Obter Dados > Banco de
Dados MySQL**) e usar as *views* já criadas no `database/constrular.sql`
(`vw_vendas`, `vw_estoque`, `vw_analise_financeira`, etc.) como fonte
direta.

## Validações de negócio

A camada de serviços (`src/services/`) valida os dados antes de
persistir no banco, entre elas:

- Funcionário: nome e cargo obrigatórios; **salário não pode ser
  negativo nem zero**.
- Produto: preço de custo e de venda não podem ser negativos; preço
  de venda não pode ser menor que o de custo.
- Cliente/Fornecedor: nome obrigatório; estado com 2 letras.
- Estoque: quantidade de entrada/saída deve ser maior que zero; saída
  não pode ultrapassar o estoque disponível.
- Venda: forma de pagamento obrigatória; cliente e funcionário
  informados precisam existir no banco.
- Item de venda: produto informado precisa existir; quantidade e
  preço unitário não podem ser inválidos.

Quando uma validação falha, o serviço levanta um `ValueError` com uma
mensagem clara, capturado pelo menu (`src/main.py`), que exibe o erro
sem derrubar o programa.

## Robustez e tratamento de erros

- **Entrada inválida não derruba o sistema.** O loop principal do menu
  (`src/main.py`) tem um `try/except` que captura tanto `ValueError`
  (ex: digitar uma letra onde era esperado um número) quanto qualquer
  outro erro inesperado (ex: erro de conexão ou de integridade do
  banco, como um CPF duplicado). O sistema volta para o menu principal
  em vez de fechar.
- **Sem vazamento de conexão.** Todas as funções em `src/repositories/`
  usam o context manager `obter_cursor()` (definido em
  `src/config/database.py`), que garante o fechamento do cursor e da
  conexão mesmo se ocorrer um erro no meio da query — e faz
  `commit`/`rollback` automaticamente para operações de escrita.
- **Validação das variáveis de ambiente.** Se o `.env` não estiver
  configurado corretamente, `conectar()` levanta um erro claro
  indicando quais variáveis estão faltando, em vez de um erro genérico
  do driver MySQL.

## Testes automatizados

O projeto tem dois tipos de teste em `tests/`:

- **`test_validacoes.py`** — testes de verdade com `pytest` e `assert`,
  usando `monkeypatch` para simular o banco. Rodam em qualquer máquina,
  sem precisar de MySQL configurado, e cobrem as regras de negócio
  descritas acima (salário negativo, preços inválidos, FK inexistente,
  estoque insuficiente, etc). Para rodar:

  ```bash
  pip install -r requirements-dev.txt
  pytest tests/test_validacoes.py -v
  ```

- **`test_estoque.py`, `test_vendas.py`, `test_item_venda.py`,
  `test_consulta_venda.py`, `test_produtos.py`** — scripts de
  demonstração manual (com `print`, sem `assert`) que exercitam os
  fluxos reais contra um banco MySQL configurado no `.env`. Servem
  para validar a integração de ponta a ponta, não como suíte
  automatizada. Para rodá-los, a partir da raiz do projeto:

  ```bash
  python -m tests.test_estoque
  ```

## Integração contínua (CI)

O repositório tem um workflow do GitHub Actions
(`.github/workflows/tests.yml`) que roda automaticamente a cada
`push` ou pull request:

1. Instala as dependências de `requirements-dev.txt`;
2. Roda `pytest tests/test_validacoes.py -v` (os 29 testes de
   validação, sem precisar de banco);
3. Verifica se todos os arquivos `.py` do projeto compilam sem erro
   de sintaxe.

Testa em Python 3.11 e 3.12. Depois de subir o projeto para o GitHub,
troque `SEU_USUARIO/SEU_REPOSITORIO` no badge no topo deste README
pelo caminho real do seu repositório, para o selo aparecer.

## Autor

Projeto acadêmico desenvolvido por Renan, aluno de Análise e
Desenvolvimento de Sistemas na FATEC Guaratinguetá.

## Licença

Este projeto está sob a licença MIT — veja o arquivo [LICENSE](LICENSE)
para mais detalhes.
