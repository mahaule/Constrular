"""
Consultas de relatórios avançados, voltadas para análise de dados
(Power BI, planilhas, dashboards).

Diferente de `src/services/relatorio_service.py` (que atende ao menu
de texto do sistema com respostas simples), este módulo devolve os
dados como `pandas.DataFrame`, prontos para:
  - exportar para CSV/Excel e importar no Power BI;
  - plugar direto num notebook para análise exploratória;
  - servir de base para novas telas/relatórios no futuro.

Executar este arquivo diretamente gera uma pasta `relatorios_exportados/`
na raiz do projeto com um CSV para cada relatório, já prontos para
serem importados como fonte de dados no Power BI (Obter Dados > Texto/CSV).
"""

import os
from decimal import Decimal

import pandas as pd

from src.config.database import conectar


def _consultar_dataframe(query):
    """
    Executa uma query e retorna o resultado como DataFrame.

    Observação técnica: a partir do pandas 2.x, `pd.read_sql()` só
    aceita conexões SQLAlchemy (ou sqlite3) — passar a conexão do
    mysql-connector-python direto não é mais suportado. Por isso,
    aqui o cursor é usado manualmente e o DataFrame é montado a
    partir de `cursor.fetchall()` + `cursor.column_names`, sem
    depender do SQLAlchemy como dependência extra do projeto.
    """
    conexao = conectar()
    try:
        cursor = conexao.cursor()
        cursor.execute(query)

        colunas = cursor.column_names
        linhas = cursor.fetchall()

        cursor.close()

        df = pd.DataFrame(linhas, columns=colunas)

        # O mysql-connector devolve colunas DECIMAL como Decimal;
        # convertendo para float aqui, o CSV exportado fica com
        # números "normais" em vez de texto, o que facilita o
        # Power BI reconhecer a coluna automaticamente como numérica.
        for coluna in df.columns:
            if df[coluna].apply(lambda v: isinstance(v, Decimal)).any():
                df[coluna] = df[coluna].astype(float)

        return df
    finally:
        conexao.close()


def faturamento_mensal():
    """Faturamento, custo e lucro agregados por mês — base para
    gráficos de tendência e sazonalidade no Power BI."""
    query = """
        SELECT
            DATE_FORMAT(v.data_venda, '%Y-%m') AS ano_mes,
            COUNT(DISTINCT v.id_venda) AS quantidade_vendas,
            SUM(iv.quantidade) AS itens_vendidos,
            SUM(iv.quantidade * iv.preco_unitario) AS faturamento,
            SUM(iv.quantidade * p.preco_custo) AS custo_total,
            SUM(iv.quantidade * iv.preco_unitario)
                - SUM(iv.quantidade * p.preco_custo) AS lucro
        FROM vendas v
        JOIN itens_venda iv ON iv.venda_id = v.id_venda
        JOIN produtos p ON p.id_produto = iv.produto_id
        GROUP BY DATE_FORMAT(v.data_venda, '%Y-%m')
        ORDER BY ano_mes
    """
    return _consultar_dataframe(query)


def faturamento_por_categoria():
    """Faturamento e lucro por categoria de produto."""
    query = """
        SELECT
            c.nome AS categoria,
            SUM(iv.quantidade) AS quantidade_vendida,
            SUM(iv.quantidade * iv.preco_unitario) AS faturamento,
            SUM(iv.quantidade * iv.preco_unitario)
                - SUM(iv.quantidade * p.preco_custo) AS lucro
        FROM itens_venda iv
        JOIN produtos p ON p.id_produto = iv.produto_id
        JOIN categorias c ON c.id_categoria = p.categoria_id
        GROUP BY c.nome
        ORDER BY faturamento DESC
    """
    return _consultar_dataframe(query)


def vendas_por_cidade():
    """Faturamento agregado pela cidade do cliente — útil para
    mapas e análise geográfica no Power BI."""
    query = """
        SELECT
            c.cidade,
            c.estado,
            COUNT(DISTINCT v.id_venda) AS quantidade_vendas,
            SUM(iv.quantidade * iv.preco_unitario) AS faturamento
        FROM vendas v
        JOIN clientes c ON c.id_cliente = v.cliente_id
        JOIN itens_venda iv ON iv.venda_id = v.id_venda
        WHERE c.cidade IS NOT NULL
        GROUP BY c.cidade, c.estado
        ORDER BY faturamento DESC
    """
    return _consultar_dataframe(query)


def ticket_medio_mensal():
    """Ticket médio (valor médio por venda) por mês."""
    query = """
        SELECT
            DATE_FORMAT(v.data_venda, '%Y-%m') AS ano_mes,
            ROUND(
                SUM(iv.quantidade * iv.preco_unitario)
                    / COUNT(DISTINCT v.id_venda),
                2
            ) AS ticket_medio
        FROM vendas v
        JOIN itens_venda iv ON iv.venda_id = v.id_venda
        GROUP BY DATE_FORMAT(v.data_venda, '%Y-%m')
        ORDER BY ano_mes
    """
    return _consultar_dataframe(query)


def desempenho_funcionarios():
    """Quantidade de vendas, faturamento gerado e ticket médio por
    funcionário — permite comparar desempenho da equipe de vendas."""
    query = """
        SELECT
            f.id_funcionario,
            f.nome AS funcionario,
            f.cargo,
            COUNT(DISTINCT v.id_venda) AS quantidade_vendas,
            SUM(iv.quantidade * iv.preco_unitario) AS faturamento_gerado,
            ROUND(
                SUM(iv.quantidade * iv.preco_unitario)
                    / NULLIF(COUNT(DISTINCT v.id_venda), 0),
                2
            ) AS ticket_medio
        FROM funcionarios f
        LEFT JOIN vendas v ON v.funcionario_id = f.id_funcionario
        LEFT JOIN itens_venda iv ON iv.venda_id = v.id_venda
        GROUP BY f.id_funcionario, f.nome, f.cargo
        ORDER BY faturamento_gerado DESC
    """
    return _consultar_dataframe(query)


def top_clientes(limite=20):
    """Ranking dos clientes que mais compraram (em valor)."""
    query = f"""
        SELECT
            cl.id_cliente,
            cl.nome AS cliente,
            cl.cidade,
            cl.estado,
            COUNT(DISTINCT v.id_venda) AS quantidade_compras,
            SUM(iv.quantidade * iv.preco_unitario) AS total_gasto
        FROM clientes cl
        JOIN vendas v ON v.cliente_id = cl.id_cliente
        JOIN itens_venda iv ON iv.venda_id = v.id_venda
        GROUP BY cl.id_cliente, cl.nome, cl.cidade, cl.estado
        ORDER BY total_gasto DESC
        LIMIT {int(limite)}
    """
    return _consultar_dataframe(query)


def ranking_margem_produtos():
    """Ranking de produtos por margem de lucro unitária e total,
    útil para identificar os produtos mais rentáveis."""
    query = """
        SELECT
            p.id_produto,
            p.nome AS produto,
            c.nome AS categoria,
            p.preco_custo,
            p.preco_venda,
            ROUND(p.preco_venda - p.preco_custo, 2) AS margem_unitaria,
            ROUND(
                100 * (p.preco_venda - p.preco_custo) / NULLIF(p.preco_custo, 0),
                1
            ) AS margem_percentual,
            COALESCE(SUM(iv.quantidade), 0) AS quantidade_vendida,
            COALESCE(
                SUM(iv.quantidade * (iv.preco_unitario - p.preco_custo)),
                0
            ) AS lucro_total
        FROM produtos p
        JOIN categorias c ON c.id_categoria = p.categoria_id
        LEFT JOIN itens_venda iv ON iv.produto_id = p.id_produto
        GROUP BY
            p.id_produto, p.nome, c.nome,
            p.preco_custo, p.preco_venda
        ORDER BY lucro_total DESC
    """
    return _consultar_dataframe(query)


def formas_pagamento_mensal():
    """Distribuição de faturamento por forma de pagamento e mês —
    útil para gráficos de composição (barras empilhadas, pizza)."""
    query = """
        SELECT
            DATE_FORMAT(v.data_venda, '%Y-%m') AS ano_mes,
            v.forma_pagamento,
            COUNT(DISTINCT v.id_venda) AS quantidade_vendas,
            SUM(iv.quantidade * iv.preco_unitario) AS faturamento
        FROM vendas v
        JOIN itens_venda iv ON iv.venda_id = v.id_venda
        GROUP BY DATE_FORMAT(v.data_venda, '%Y-%m'), v.forma_pagamento
        ORDER BY ano_mes, faturamento DESC
    """
    return _consultar_dataframe(query)


def situacao_estoque():
    """Situação atual do estoque de cada produto (via a view
    `vw_estoque` já existente no banco), incluindo o valor de
    custo parado em estoque — útil para análise de capital de giro."""
    query = """
        SELECT
            id_produto,
            produto,
            categoria,
            fornecedor,
            preco_custo,
            preco_venda,
            estoque_minimo,
            estoque_atual,
            status_estoque,
            ROUND(preco_custo * estoque_atual, 2) AS valor_custo_em_estoque
        FROM vw_estoque
        ORDER BY status_estoque, estoque_atual ASC
    """
    return _consultar_dataframe(query)


def folha_pagamento_por_cargo():
    """Total de salários e headcount por cargo — dado simples de
    RH útil para um painel de custos operacionais."""
    query = """
        SELECT
            cargo,
            COUNT(*) AS quantidade_funcionarios,
            SUM(salario) AS total_salarios,
            ROUND(AVG(salario), 2) AS salario_medio
        FROM funcionarios
        GROUP BY cargo
        ORDER BY total_salarios DESC
    """
    return _consultar_dataframe(query)


# Registro central de todos os relatórios disponíveis, usado tanto
# pela exportação em massa (main()) quanto por quem quiser importar
# só o dicionário e escolher um relatório específico.
RELATORIOS = {
    "faturamento_mensal": faturamento_mensal,
    "faturamento_por_categoria": faturamento_por_categoria,
    "vendas_por_cidade": vendas_por_cidade,
    "ticket_medio_mensal": ticket_medio_mensal,
    "desempenho_funcionarios": desempenho_funcionarios,
    "top_clientes": top_clientes,
    "ranking_margem_produtos": ranking_margem_produtos,
    "formas_pagamento_mensal": formas_pagamento_mensal,
    "situacao_estoque": situacao_estoque,
    "folha_pagamento_por_cargo": folha_pagamento_por_cargo,
}


def exportar_todos_para_csv(pasta_destino="relatorios_exportados"):
    """Executa todos os relatórios acima e salva cada um como um
    arquivo CSV separado, pronto para ser importado no Power BI
    (Obter Dados > Texto/CSV) ou aberto no Excel."""
    os.makedirs(pasta_destino, exist_ok=True)

    for nome, funcao in RELATORIOS.items():
        print(f"Gerando relatório: {nome}...")
        df = funcao()
        caminho = os.path.join(pasta_destino, f"{nome}.csv")
        df.to_csv(caminho, index=False, encoding="utf-8-sig")
        print(f"  -> {len(df)} linhas salvas em {caminho}")

    print(f"\nTodos os relatórios foram exportados para '{pasta_destino}/'.")
    print("No Power BI: Obter Dados > Texto/CSV > selecione os arquivos.")


if __name__ == "__main__":
    exportar_todos_para_csv()
