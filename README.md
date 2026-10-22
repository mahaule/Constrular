# Constrular — Sistema de Gestão Comercial

[![Testes](https://github.com/mahaule/Constrular/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/mahaule/Constrular/actions/workflows/tests.yml)

Sistema de linha de comando (CLI) desenvolvido em Python para a gestão de uma loja de materiais de construção, com banco de dados MySQL, controle de estoque, registro de vendas e relatórios gerenciais.

O projeto também oferece consultas analíticas e geração de arquivos CSV para apoiar a criação de dashboards no Power BI.

## Funcionalidades

- **Produtos:** cadastro, consulta, atualização e exclusão.
- **Clientes:** gerenciamento de clientes.
- **Fornecedores:** cadastro e consulta de fornecedores.
- **Funcionários:** gerenciamento de funcionários e salários.
- **Vendas:** registro de vendas, inclusão de itens e consulta de informações.
- **Estoque:** consulta de estoque e registro de entradas e saídas.
- **Relatórios:** total de vendas, faturamento, produtos mais vendidos e estoque baixo.
- **Análises de dados:** consultas SQL para análise financeira, comercial e operacional.
- **Dados mockados:** geração de histórico fictício para explorar tendências, sazonalidade e indicadores no Power BI.

## Tecnologias utilizadas

- Python 3.11+
- MySQL 8.0+
- SQL
- pandas
- pytest
- python-dotenv
- Git e GitHub Actions
- Power BI Desktop — para visualização e análise dos dados

## Arquitetura do projeto

O sistema utiliza uma arquitetura organizada em camadas, separando a interface de terminal, as regras de negócio e o acesso ao banco de dados.

```text
Constrular/
├── .github/
│   └── workflows/
│       └── tests.yml
├── database/
│   └── constrular.sql
├── scripts/
│   └── popular_banco.py
├── src/
│   ├── config/
│   │   └── database.py
│   ├── models/
│   ├── queries/
│   │   └── relatorios.py
│   ├── repositories/
│   ├── services/
│   └── main.py
├── tests/
├── .env.example
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── requirements-dev.txt
```

### Responsabilidades das camadas

- **Config:** configuração da conexão com o banco de dados.
- **Models:** classes que representam as entidades do domínio.
- **Repositories:** execução de consultas SQL e operações de persistência.
- **Services:** regras de negócio e validações.
- **Queries:** consultas analíticas que retornam DataFrames e permitem exportação para CSV.
- **Main:** menu interativo que permite utilizar as funcionalidades pelo terminal.
- **Scripts:** geração de dados fictícios para análises.
- **Tests:** testes automatizados e scripts de demonstração das funcionalidades.

O fluxo principal de execução é:

`main.py → services → repositories → config`

## Pré-requisitos

Antes de executar o projeto, instale:

- Python 3.11 ou superior.
- MySQL Server 8.0 ou superior.
- Git.

Para utilizar a conexão direta do Power BI Desktop com o MySQL, também pode ser necessário instalar o Oracle MySQL Connector/NET.

## Configuração e instalação

### 1. Clone o repositório

```bash
git clone https://github.com/mahaule/Constrular.git
cd Constrular
```

### 2. Crie e ative o ambiente virtual

**Windows — PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux ou macOS:**

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
python -m pip install -r requirements.txt
```

Para instalar também as dependências de desenvolvimento e testes:

```bash
python -m pip install -r requirements-dev.txt
```

### 4. Configure as variáveis de ambiente

Copie o arquivo `.env.example` para um novo arquivo chamado `.env`.

**Windows — PowerShell:**

```powershell
Copy-Item .env.example .env
```

**Linux ou macOS:**

```bash
cp .env.example .env
```

Abra o arquivo `.env` e configure as credenciais do seu MySQL:

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=sua_senha
DB_NAME=constrular
```

Substitua `sua_senha` pela senha do seu usuário MySQL.

> **Segurança:** nunca publique o arquivo `.env` com sua senha real. Ele está protegido pelo `.gitignore`. O arquivo `.env.example` deve ser utilizado como modelo, sem credenciais reais.

### 5. Crie e importe o banco de dados

Primeiro, crie o schema no MySQL Workbench executando:

```sql
CREATE DATABASE IF NOT EXISTS constrular
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_0900_ai_ci;
```

Em seguida:

1. Atualize a lista de schemas do Workbench.
2. Selecione o schema `constrular` como schema padrão.
3. Abra o arquivo `database/constrular.sql`.
4. Confirme que o schema padrão selecionado é `constrular` antes de executar o script inteiro.

O arquivo SQL cria as tabelas, insere os dados iniciais e define as views utilizadas nas análises.

> **Atenção:** o script contém comandos que apagam e recriam tabelas e views. Importe-o em um schema de teste vazio para não perder dados importantes. O dump não cria nem seleciona automaticamente o schema de destino.

## Como executar o sistema

Com o banco configurado, o MySQL em execução e o arquivo `.env` preenchido, execute a partir da raiz do projeto:

```bash
python -m src.main
```

O sistema abre um menu interativo no terminal, com opções para gerenciar produtos, clientes, fornecedores, funcionários, vendas e estoque, além de consultar relatórios.

## Gerando dados mockados para o Power BI

O banco inicial contém um conjunto pequeno de dados fictícios, suficiente para testar as funcionalidades básicas, mas limitado para análises de tendências, sazonalidade e rankings.

Para ampliar a base de dados, execute:

```bash
python -m scripts.popular_banco
```

O script solicita confirmação antes de começar e adiciona dados fictícios ao banco configurado no `.env`, incluindo:

- Aproximadamente 12 meses de histórico de vendas.
- Cerca de 75 clientes distribuídos em cidades do Vale do Paraíba.
- 30 produtos adicionais, distribuídos nas categorias existentes.
- Cinco fornecedores adicionais.
- Sete funcionários adicionais, com diferentes cargos e salários.
- Centenas de vendas, com vários itens e preços que simulam pequenas variações comerciais.
- Movimentações de estoque de entrada e saída, considerando o estoque disponível durante a simulação.

O histórico inclui uma variação sazonal simples, com maior volume de vendas previsto para novembro e dezembro e menor volume em fevereiro.

O script utiliza uma transação para inserir os dados e executa `ROLLBACK` quando ocorre um erro durante a operação.

> **Importante:** execute o script apenas uma vez em cada banco preparado. Ele acrescenta registros e pode duplicar dados se for executado novamente. Se precisar repetir a simulação, utilize um banco de teste recriado a partir do dump inicial.

## Exportando relatórios para o Power BI

O módulo `src/queries/relatorios.py` disponibiliza consultas analíticas que retornam DataFrames do pandas e podem ser exportados para CSV.

Execute:

```bash
python -m src.queries.relatorios
```

Os arquivos são gerados na pasta `relatorios_exportados/`, na raiz do projeto.

| Arquivo CSV | Conteúdo |
|---|---|
| `faturamento_mensal.csv` | Faturamento, custo e lucro por mês |
| `faturamento_por_categoria.csv` | Faturamento e lucro por categoria |
| `vendas_por_cidade.csv` | Faturamento por cidade do cliente |
| `ticket_medio_mensal.csv` | Ticket médio mensal |
| `desempenho_funcionarios.csv` | Vendas, faturamento e ticket médio por funcionário |
| `top_clientes.csv` | Ranking dos clientes que mais compraram |
| `ranking_margem_produtos.csv` | Margem de lucro por produto |
| `formas_pagamento_mensal.csv` | Faturamento por forma de pagamento e mês |
| `situacao_estoque.csv` | Estoque atual, status e valor de custo parado |
| `folha_pagamento_por_cargo.csv` | Total de salários e quantidade de funcionários por cargo |

### Opção 1 — Importar arquivos CSV

No Power BI Desktop, selecione **Obter dados → Texto/CSV**, escolha os arquivos desejados e carregue os dados para construir os relatórios.

### Opção 2 — Conectar diretamente ao MySQL

Também é possível conectar o Power BI Desktop diretamente ao banco de dados MySQL.

Selecione **Obter dados → Banco de dados MySQL** e utilize o servidor, o nome do banco e as credenciais correspondentes ao seu ambiente.

O banco disponibiliza as seguintes views analíticas:

- `vw_vendas`
- `vw_estoque`
- `vw_analise_financeira`
- `vw_produtos_mais_vendidos`
- `vw_faturamento_funcionarios`
- `vw_faturamento_pagamento`

Essas views podem servir como fonte para gráficos de faturamento, rentabilidade, produtos mais vendidos, desempenho comercial e controle de estoque.

## Validações de negócio

A camada `services` valida os dados antes de persistir as informações no banco.

Entre as regras implementadas estão:

- **Funcionários:** nome e cargo obrigatórios; salário deve ser positivo.
- **Produtos:** preços não negativos e preço de venda não inferior ao preço de custo.
- **Clientes e fornecedores:** nome obrigatório e validações dos campos informados, incluindo o estado.
- **Estoque:** entradas e saídas com quantidades positivas; saídas limitadas pelo estoque disponível.
- **Vendas:** forma de pagamento obrigatória e validação da existência de clientes e funcionários informados.
- **Itens de venda:** validação do produto, da quantidade e do preço unitário.

Quando uma validação falha, os serviços lançam `ValueError` com uma mensagem explicativa para que o menu possa apresentar o erro ao usuário.

## Robustez e tratamento de erros

O projeto inclui mecanismos para tornar a execução mais segura:

- Tratamento de entradas inválidas e erros inesperados no menu.
- Gerenciamento centralizado de conexões e cursores por meio de `obter_cursor()`, em `src/config/database.py`.
- Fechamento de conexões e cursores mesmo quando uma consulta falha.
- `commit` para operações de escrita e `rollback` em caso de erro durante transações gerenciadas pelo context manager.
- Verificação das variáveis obrigatórias do arquivo `.env`, com mensagens indicando as configurações ausentes.

## Testes

O projeto possui testes automatizados e scripts de demonstração manual.

### Testes automatizados

O arquivo `tests/test_validacoes.py` contém 29 testes com pytest, cobrindo as regras de negócio e utilizando simulações para testar os serviços sem depender de uma conexão real com o MySQL.

Para executar:

```bash
python -m pip install -r requirements-dev.txt
python -m pytest tests/test_validacoes.py -v
```

### Demonstrações manuais

Os arquivos `test_estoque.py`, `test_vendas.py`, `test_item_venda.py`, `test_consulta_venda.py` e `test_produtos.py` demonstram operações reais do sistema.

Esses scripts utilizam o banco configurado no `.env` e podem inserir ou modificar dados. Execute-os somente em um banco de desenvolvimento ou teste.

Exemplo:

```bash
python -m tests.test_estoque
```

## Integração contínua

O projeto utiliza GitHub Actions por meio do workflow `.github/workflows/tests.yml`.

O pipeline é executado em eventos de `push`, pull requests e também pode ser iniciado manualmente pela aba **Actions** do GitHub.

As etapas incluem:

1. Configuração dos ambientes Python 3.11 e 3.12.
2. Instalação das dependências de desenvolvimento.
3. Execução dos testes automatizados de validação.
4. Verificação de sintaxe dos arquivos Python.

O selo de testes no início deste README exibe o status do workflow configurado para o repositório.

## Segurança dos dados

Os dados utilizados para demonstração devem ser fictícios. Não publique senhas, credenciais de conexão, dados pessoais reais ou informações de clientes.

O arquivo `.env` é ignorado pelo Git, enquanto o `.env.example` contém apenas os nomes das variáveis necessárias para configurar a conexão.

## Autor

Projeto acadêmico desenvolvido por **Renan dos Santos Freitas**, estudante de Análise e Desenvolvimento de Sistemas na FATEC Guaratinguetá.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais informações.