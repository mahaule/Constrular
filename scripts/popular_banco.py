"""
Script de geração de dados mockados para o banco `constrular`.

Objetivo
--------
Popular o banco com um volume de dados realista (~12 meses de histórico
de vendas, clientes de várias cidades do Vale do Paraíba, produtos,
funcionários e movimentações de estoque) para que seja possível montar
relatórios e dashboards no Power BI com dados suficientes para gerar
gráficos de tendência, sazonalidade, ranking, etc.

Este script assume que o schema já foi criado a partir de
`database/constrular.sql` (que já traz 5 registros de exemplo em cada
tabela). Ele ADICIONA novos registros por cima dos existentes — não
apaga nada. Pode ser executado novamente, mas isso vai duplicar os
dados (ele não é idempotente de propósito, para manter o script simples).

Como executar
--------------
    python -m scripts.popular_banco

(execute a partir da raiz do projeto, com o ambiente virtual e o
arquivo .env configurados)
"""

import random
from datetime import datetime, timedelta

from src.config.database import conectar


# =============================================================
# CONFIGURAÇÃO
# =============================================================

random.seed(42)  # reprodutibilidade: rode de novo e terá os mesmos dados

MESES_DE_HISTORICO = 12
DATA_FINAL = datetime.now()
DATA_INICIAL = DATA_FINAL - timedelta(days=30 * MESES_DE_HISTORICO)

# Sazonalidade simples: multiplicador de vendas por mês (1 = normal).
# Novembro/Dezembro mais fortes (reformas de fim de ano), fevereiro mais fraco.
PESO_SAZONAL_POR_MES = {
    1: 0.9, 2: 0.75, 3: 0.95, 4: 1.0, 5: 1.05, 6: 1.0,
    7: 1.0, 8: 1.05, 9: 1.1, 10: 1.15, 11: 1.3, 12: 1.35,
}

VENDAS_BASE_POR_DIA_UTIL = 3  # média de vendas em um dia "normal"


# =============================================================
# DADOS DE APOIO PARA GERAÇÃO ALEATÓRIA
# =============================================================

CIDADES_VALE_DO_PARAIBA = [
    ("Guaratinguetá", "SP"),
    ("Pindamonhangaba", "SP"),
    ("Taubaté", "SP"),
    ("Lorena", "SP"),
    ("São José dos Campos", "SP"),
    ("Aparecida", "SP"),
    ("Cruzeiro", "SP"),
    ("Cachoeira Paulista", "SP"),
    ("Jacareí", "SP"),
    ("Caçapava", "SP"),
    ("Tremembé", "SP"),
    ("Roseira", "SP"),
]

PRIMEIROS_NOMES = [
    "João", "Maria", "Carlos", "Ana", "Pedro", "Juliana", "Lucas",
    "Fernanda", "Marcos", "Patrícia", "Rafael", "Camila", "Bruno",
    "Aline", "Diego", "Larissa", "Thiago", "Vanessa", "Rodrigo",
    "Beatriz", "Gustavo", "Renata", "Felipe", "Priscila", "André",
    "Tatiane", "Eduardo", "Simone", "Leandro", "Débora", "Fábio",
    "Cristina", "Vinícius", "Adriana", "Marcelo", "Sandra", "Anderson",
    "Roberta", "William", "Elaine",
]

SOBRENOMES = [
    "Silva", "Santos", "Oliveira", "Souza", "Costa", "Pereira",
    "Almeida", "Ferreira", "Rodrigues", "Martins", "Carvalho",
    "Gomes", "Ribeiro", "Barbosa", "Araújo", "Lima", "Nascimento",
    "Moreira", "Nunes", "Teixeira", "Cardoso", "Correia", "Dias",
    "Machado", "Castro",
]

CARGOS_FUNCIONARIOS = [
    ("Gerente", 4500.00, 6000.00),
    ("Vendedor", 2200.00, 3200.00),
    ("Vendedora", 2200.00, 3200.00),
    ("Caixa", 2000.00, 2800.00),
    ("Estoquista", 1900.00, 2600.00),
    ("Auxiliar Administrativo", 2000.00, 2700.00),
]

FORMAS_PAGAMENTO = [
    "PIX", "PIX", "PIX",
    "Cartao de Credito", "Cartao de Credito",
    "Cartao de Debito",
    "Dinheiro",
    "Boleto",
]

# Categorias já existentes no banco (id, nome) — ver database/constrular.sql
CATEGORIAS = {
    1: "Materiais de Construção",
    2: "Ferramentas",
    3: "Elétrica",
    4: "Hidráulica",
    5: "Pintura",
}

# Produtos adicionais por categoria: (nome, descricao, preco_custo, preco_venda, estoque_minimo)
PRODUTOS_NOVOS = {
    1: [
        ("Cimento CP-V 50kg", "Cimento de alta resistência inicial, saco de 50kg", 32.00, 44.90, 20),
        ("Areia Média m³", "Areia média lavada, granel", 55.00, 79.90, 10),
        ("Brita 1 m³", "Brita número 1 para concreto", 60.00, 89.90, 10),
        ("Bloco de Concreto 14x19x39", "Bloco estrutural de concreto", 2.80, 4.50, 200),
        ("Telha Cerâmica Portuguesa", "Telha cerâmica modelo português, unidade", 1.90, 3.20, 300),
        ("Cal Hidratada 20kg", "Cal hidratada para argamassa", 12.00, 18.90, 30),
    ],
    2: [
        ("Serra Circular 7 1/4\"", "Serra circular elétrica 1500W", 220.00, 349.90, 5),
        ("Chave de Fenda 6mm", "Chave de fenda cabo emborrachado", 8.00, 15.90, 20),
        ("Trena 5m", "Trena com trava automática 5 metros", 14.00, 24.90, 15),
        ("Nível de Bolha 40cm", "Nível de bolha em alumínio", 18.00, 29.90, 15),
        ("Alicate Universal 8\"", "Alicate universal cabo isolado", 22.00, 38.90, 15),
        ("Parafusadeira a Bateria", "Parafusadeira/furadeira 12V com maleta", 150.00, 249.90, 6),
    ],
    3: [
        ("Fio Flexível 4mm", "Rolo de fio elétrico flexível 4mm 100m", 145.00, 219.90, 8),
        ("Fita Isolante 20m", "Fita isolante antichama", 4.00, 8.90, 40),
        ("Tomada 20A", "Tomada padrão novo NBR 20A", 9.00, 16.90, 30),
        ("Interruptor Simples", "Interruptor simples com placa", 7.50, 14.90, 30),
        ("Lâmpada LED 12W", "Lâmpada LED bivolt luz branca", 8.00, 16.90, 40),
        ("Quadro de Distribuição 12 Disjuntores", "Quadro de distribuição embutir", 65.00, 109.90, 8),
    ],
    4: [
        ("Tubo PVC 50mm", "Tubo PVC esgoto 50mm barra 6m", 28.00, 42.90, 12),
        ("Joelho PVC 90° 25mm", "Conexão joelho 90 graus 25mm", 2.00, 4.50, 50),
        ("Registro de Gaveta 3/4", "Registro de gaveta bruto 3/4 polegada", 22.00, 38.90, 15),
        ("Caixa D'água 500L", "Caixa d'água em polietileno 500 litros", 220.00, 329.90, 4),
        ("Sifão Sanfonado", "Sifão sanfonado para pia", 9.00, 17.90, 20),
        ("Mangueira de Silicone 1m", "Mangueira flexível para conexão hidráulica", 6.00, 12.90, 25),
    ],
    5: [
        ("Tinta Esmalte Sintético 3,6L", "Tinta esmalte brilhante para madeira e metal", 65.00, 99.90, 10),
        ("Massa Corrida 25kg", "Massa corrida PVA para paredes internas", 35.00, 54.90, 12),
        ("Lixa para Parede Grão 100", "Lixa em folha para preparação de parede", 1.50, 3.20, 50),
        ("Pincel 2 1/2\"", "Pincel para pintura em madeira e metal", 6.00, 11.90, 30),
        ("Fita Crepe 48mm", "Fita crepe para acabamento em pintura", 5.00, 9.90, 40),
        ("Verniz Marítimo 900ml", "Verniz marítimo brilhante para madeira", 28.00, 44.90, 15),
    ],
}

FORNECEDORES_NOVOS = [
    ("Distribuidora Vale Materiais", "(12) 99999-2001", "contato@valemateriais.com", "Taubaté", "SP"),
    ("Ferragens São José", "(12) 99999-2002", "vendas@ferragenssj.com", "São José dos Campos", "SP"),
    ("Elétrica Guará", "(12) 99999-2003", "contato@eletricaguara.com", "Guaratinguetá", "SP"),
    ("Hidráulica Jacareí", "(12) 99999-2004", "vendas@hidraulicajacarei.com", "Jacareí", "SP"),
    ("Tintas & Cia Pinda", "(12) 99999-2005", "contato@tintasecia.com", "Pindamonhangaba", "SP"),
]


def gerar_cpf_fake():
    """Gera uma string no formato de CPF (não é um CPF matematicamente válido,
    mas serve como identificador único fictício para dados de teste)."""
    n = [random.randint(0, 9) for _ in range(9)]
    return (
        f"{n[0]}{n[1]}{n[2]}.{n[3]}{n[4]}{n[5]}.{n[6]}{n[7]}{n[8]}-"
        f"{random.randint(10, 99)}"
    )


def gerar_telefone():
    return f"(12) 9{random.randint(6000, 9999)}-{random.randint(1000, 9999)}"


def data_aleatoria_no_mes(ano, mes):
    """Retorna um datetime aleatório dentro do mês/ano informado."""
    if mes == 12:
        proximo_mes = datetime(ano + 1, 1, 1)
    else:
        proximo_mes = datetime(ano, mes + 1, 1)

    primeiro_dia = datetime(ano, mes, 1)
    dias_no_mes = (proximo_mes - primeiro_dia).days

    dia = random.randint(1, dias_no_mes)
    hora = random.randint(8, 19)
    minuto = random.randint(0, 59)

    return datetime(ano, mes, dia, hora, minuto)


def meses_do_periodo(data_inicial, data_final):
    """Gera tuplas (ano, mes) entre as duas datas, inclusive."""
    atual = datetime(data_inicial.year, data_inicial.month, 1)
    fim = datetime(data_final.year, data_final.month, 1)

    resultado = []
    while atual <= fim:
        resultado.append((atual.year, atual.month))
        if atual.month == 12:
            atual = datetime(atual.year + 1, 1, 1)
        else:
            atual = datetime(atual.year, atual.month + 1, 1)

    return resultado


# =============================================================
# FUNÇÕES DE POPULAÇÃO
# =============================================================

def popular_fornecedores(cursor):
    print("Inserindo fornecedores adicionais...")

    ids = []
    for nome, telefone, email, cidade, estado in FORNECEDORES_NOVOS:
        cursor.execute(
            """
            INSERT INTO fornecedores (nome, telefone, email, cidade, estado)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (nome, telefone, email, cidade, estado),
        )
        ids.append(cursor.lastrowid)

    print(f"  {len(ids)} fornecedores inseridos.")
    return ids


def popular_produtos(cursor, ids_fornecedores_existentes):
    print("Inserindo produtos adicionais...")

    todos_fornecedores = ids_fornecedores_existentes
    ids_produtos = []

    for categoria_id, lista_produtos in PRODUTOS_NOVOS.items():
        for nome, descricao, custo, venda, estoque_minimo in lista_produtos:
            fornecedor_id = random.choice(todos_fornecedores)

            cursor.execute(
                """
                INSERT INTO produtos (
                    nome, descricao, preco_custo, preco_venda,
                    estoque_minimo, categoria_id, fornecedor_id
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (nome, descricao, custo, venda, estoque_minimo,
                 categoria_id, fornecedor_id),
            )
            ids_produtos.append(cursor.lastrowid)

    print(f"  {len(ids_produtos)} produtos inseridos.")
    return ids_produtos


def popular_funcionarios(cursor, quantidade=7):
    print("Inserindo funcionários adicionais...")

    ids = []
    nomes_usados = set()

    for _ in range(quantidade):
        while True:
            nome = f"{random.choice(PRIMEIROS_NOMES)} {random.choice(SOBRENOMES)}"
            if nome not in nomes_usados:
                nomes_usados.add(nome)
                break

        cargo, salario_min, salario_max = random.choice(CARGOS_FUNCIONARIOS)
        salario = round(random.uniform(salario_min, salario_max), 2)
        telefone = gerar_telefone()

        cursor.execute(
            """
            INSERT INTO funcionarios (nome, cargo, salario, telefone)
            VALUES (%s, %s, %s, %s)
            """,
            (nome, cargo, salario, telefone),
        )
        ids.append(cursor.lastrowid)

    print(f"  {len(ids)} funcionários inseridos.")
    return ids


def popular_clientes(cursor, quantidade=75):
    print("Inserindo clientes adicionais...")

    ids = []
    nomes_usados = set()

    for _ in range(quantidade):
        while True:
            nome = f"{random.choice(PRIMEIROS_NOMES)} {random.choice(SOBRENOMES)}"
            if nome not in nomes_usados:
                nomes_usados.add(nome)
                break

        cidade, estado = random.choice(CIDADES_VALE_DO_PARAIBA)
        cpf = gerar_cpf_fake()
        telefone = gerar_telefone()
        email = (
            f"{nome.lower().replace(' ', '.')}"
            f"{random.randint(1, 999)}@email.com"
        )

        cursor.execute(
            """
            INSERT INTO clientes (nome, cpf, telefone, email, cidade, estado)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (nome, cpf, telefone, email, cidade, estado),
        )
        ids.append(cursor.lastrowid)

    print(f"  {len(ids)} clientes inseridos.")
    return ids


def estoque_inicial(cursor, ids_produtos_todos):
    """Registra uma grande entrada inicial de estoque para todos os
    produtos (novos e já existentes) no início do período simulado,
    para garantir que haverá estoque suficiente para as vendas."""
    print("Registrando estoque inicial...")

    data_inicial_str = DATA_INICIAL.strftime("%Y-%m-%d %H:%M:%S")
    estoque_simulado = {}

    for produto_id in ids_produtos_todos:
        quantidade = random.randint(150, 400)

        cursor.execute(
            """
            INSERT INTO movimentacoes_estoque (
                produto_id, tipo, quantidade, data_movimentacao, observacao
            )
            VALUES (%s, 'ENTRADA', %s, %s, %s)
            """,
            (produto_id, quantidade, data_inicial_str,
             "Estoque inicial (carga de dados de teste)"),
        )

        estoque_simulado[produto_id] = quantidade

    print(f"  Estoque inicial registrado para {len(ids_produtos_todos)} produtos.")
    return estoque_simulado


def restock_periodico(cursor, produto_id, data_venda, estoque_simulado):
    """Se o estoque de um produto estiver baixo, registra uma nova
    entrada (reposição) antes da data da venda."""
    quantidade = random.randint(80, 250)
    data_str = (data_venda - timedelta(hours=random.randint(1, 48))).strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    cursor.execute(
        """
        INSERT INTO movimentacoes_estoque (
            produto_id, tipo, quantidade, data_movimentacao, observacao
        )
        VALUES (%s, 'ENTRADA', %s, %s, %s)
        """,
        (produto_id, quantidade, data_str, "Reposição de estoque"),
    )

    estoque_simulado[produto_id] = estoque_simulado.get(produto_id, 0) + quantidade


def popular_vendas(
    cursor,
    ids_clientes,
    ids_funcionarios,
    ids_produtos_todos,
    precos_produtos,
    estoque_simulado,
):
    print("Gerando vendas ao longo do período histórico...")

    total_vendas = 0
    total_itens = 0

    for ano, mes in meses_do_periodo(DATA_INICIAL, DATA_FINAL):
        peso = PESO_SAZONAL_POR_MES.get(mes, 1.0)
        dias_uteis_aprox = 22
        vendas_no_mes = max(
            5,
            int(VENDAS_BASE_POR_DIA_UTIL * dias_uteis_aprox * peso)
        )

        for _ in range(vendas_no_mes):
            data_venda = data_aleatoria_no_mes(ano, mes)

            # Não gerar vendas no futuro além da data final real
            if data_venda > DATA_FINAL:
                continue

            cliente_id = random.choice(ids_clientes)
            funcionario_id = random.choice(ids_funcionarios)
            forma_pagamento = random.choice(FORMAS_PAGAMENTO)

            cursor.execute(
                """
                INSERT INTO vendas (
                    data_venda, cliente_id, funcionario_id, forma_pagamento
                )
                VALUES (%s, %s, %s, %s)
                """,
                (data_venda.strftime("%Y-%m-%d %H:%M:%S"),
                 cliente_id, funcionario_id, forma_pagamento),
            )
            venda_id = cursor.lastrowid

            qtd_itens = random.randint(1, 4)
            produtos_da_venda = random.sample(
                ids_produtos_todos, k=min(qtd_itens, len(ids_produtos_todos))
            )

            for produto_id in produtos_da_venda:
                quantidade = random.randint(1, 5)

                # Garante estoque suficiente antes de vender
                if estoque_simulado.get(produto_id, 0) < quantidade:
                    restock_periodico(
                        cursor, produto_id, data_venda, estoque_simulado
                    )

                preco_base = precos_produtos[produto_id]
                # pequena variação de preço (promoções/negociação), +-5%
                variacao = random.uniform(-0.05, 0.05)
                preco_unitario = round(preco_base * (1 + variacao), 2)

                cursor.execute(
                    """
                    INSERT INTO itens_venda (
                        venda_id, produto_id, quantidade, preco_unitario
                    )
                    VALUES (%s, %s, %s, %s)
                    """,
                    (venda_id, produto_id, quantidade, preco_unitario),
                )

                data_saida_str = data_venda.strftime("%Y-%m-%d %H:%M:%S")
                cursor.execute(
                    """
                    INSERT INTO movimentacoes_estoque (
                        produto_id, tipo, quantidade,
                        data_movimentacao, observacao
                    )
                    VALUES (%s, 'SAIDA', %s, %s, %s)
                    """,
                    (produto_id, quantidade, data_saida_str,
                     f"Venda #{venda_id}"),
                )

                estoque_simulado[produto_id] -= quantidade
                total_itens += 1

            total_vendas += 1

    print(f"  {total_vendas} vendas geradas, com {total_itens} itens no total.")


# =============================================================
# EXECUÇÃO PRINCIPAL
# =============================================================

def main():
    print("=" * 60)
    print(" POPULAÇÃO DE DADOS MOCKADOS - CONSTRULAR")
    print("=" * 60)
    print(
        f"Período simulado: "
        f"{DATA_INICIAL.strftime('%d/%m/%Y')} a {DATA_FINAL.strftime('%d/%m/%Y')}"
    )

    resposta = input(
        "\nIsso vai ADICIONAR dados fictícios ao banco configurado no "
        ".env. Deseja continuar? (S/N): "
    )
    if resposta.strip().upper() != "S":
        print("Operação cancelada.")
        return

    conexao = conectar()
    cursor = conexao.cursor()

    try:
        # IDs de fornecedores/produtos já existentes no dump original
        cursor.execute("SELECT id_fornecedor FROM fornecedores")
        ids_fornecedores_existentes = [r[0] for r in cursor.fetchall()]

        cursor.execute("SELECT id_produto, preco_venda FROM produtos")
        produtos_existentes = cursor.fetchall()
        ids_produtos_existentes = [r[0] for r in produtos_existentes]
        precos_produtos = {r[0]: float(r[1]) for r in produtos_existentes}

        ids_fornecedores_novos = popular_fornecedores(cursor)
        ids_fornecedores_todos = (
            ids_fornecedores_existentes + ids_fornecedores_novos
        )

        ids_produtos_novos = popular_produtos(cursor, ids_fornecedores_todos)

        # Atualiza o dicionário de preços com os produtos novos
        cursor.execute("SELECT id_produto, preco_venda FROM produtos")
        for produto_id, preco_venda in cursor.fetchall():
            precos_produtos[produto_id] = float(preco_venda)

        ids_produtos_todos = ids_produtos_existentes + ids_produtos_novos

        ids_funcionarios_novos = popular_funcionarios(cursor)
        cursor.execute("SELECT id_funcionario FROM funcionarios")
        ids_funcionarios_todos = [r[0] for r in cursor.fetchall()]

        ids_clientes_novos = popular_clientes(cursor)
        cursor.execute("SELECT id_cliente FROM clientes")
        ids_clientes_todos = [r[0] for r in cursor.fetchall()]

        estoque_simulado = estoque_inicial(cursor, ids_produtos_todos)

        popular_vendas(
            cursor,
            ids_clientes_todos,
            ids_funcionarios_todos,
            ids_produtos_todos,
            precos_produtos,
            estoque_simulado,
        )

        conexao.commit()
        print("\nDados mockados inseridos com sucesso!")
        print("O banco agora tem histórico suficiente para montar")
        print("relatórios de tendência, sazonalidade e ranking no Power BI.")

    except Exception as erro:
        conexao.rollback()
        print(f"\nErro ao popular o banco. Alterações desfeitas. Detalhe: {erro}")
        raise

    finally:
        cursor.close()
        conexao.close()


if __name__ == "__main__":
    main()
