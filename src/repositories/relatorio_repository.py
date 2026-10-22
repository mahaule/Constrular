from src.config.database import obter_cursor


def consultar_total_vendas():
    with obter_cursor() as cursor:
        cursor.execute("""
            SELECT COUNT(*)
            FROM vendas
        """)

        return cursor.fetchone()[0]


def consultar_produtos_mais_vendidos():
    with obter_cursor() as cursor:
        cursor.execute("""
            SELECT
                p.nome,
                SUM(iv.quantidade) AS quantidade_vendida
            FROM itens_venda iv
            INNER JOIN produtos p
                ON p.id_produto = iv.produto_id
            GROUP BY p.id_produto, p.nome
            ORDER BY quantidade_vendida DESC
        """)

        return cursor.fetchall()


def consultar_estoque_baixo():
    with obter_cursor() as cursor:
        cursor.execute("""
            SELECT
                p.id_produto,
                p.nome,
                COALESCE(
                    SUM(
                        CASE
                            WHEN me.tipo = 'ENTRADA' THEN me.quantidade
                            WHEN me.tipo = 'SAIDA' THEN -me.quantidade
                            ELSE 0
                        END
                    ),
                    0
                ) AS estoque,
                p.estoque_minimo
            FROM produtos p
            LEFT JOIN movimentacoes_estoque me
                ON me.produto_id = p.id_produto
            GROUP BY
                p.id_produto,
                p.nome,
                p.estoque_minimo
            HAVING estoque <= p.estoque_minimo
            ORDER BY estoque ASC
        """)

        return cursor.fetchall()


def consultar_faturamento_total():
    with obter_cursor() as cursor:
        cursor.execute("""
            SELECT COALESCE(
                SUM(iv.quantidade * iv.preco_unitario),
                0
            )
            FROM itens_venda iv
        """)

        return cursor.fetchone()[0]
