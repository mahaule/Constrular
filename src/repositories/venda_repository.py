from src.config.database import obter_cursor


def listar_vendas():
    with obter_cursor() as cursor:
        cursor.execute("""
            SELECT
                id_venda,
                data_venda,
                cliente_id,
                funcionario_id,
                forma_pagamento
            FROM vendas
            ORDER BY id_venda
        """)

        return cursor.fetchall()


def buscar_venda_por_id(id_venda):
    with obter_cursor() as cursor:
        cursor.execute("""
            SELECT
                id_venda,
                data_venda,
                cliente_id,
                funcionario_id,
                forma_pagamento
            FROM vendas
            WHERE id_venda = %s
        """, (id_venda,))

        return cursor.fetchone()


def cadastrar_venda(
    cliente_id,
    funcionario_id,
    forma_pagamento
):
    with obter_cursor(commit=True) as cursor:
        cursor.execute("""
            INSERT INTO vendas (
                cliente_id,
                funcionario_id,
                forma_pagamento
            )
            VALUES (%s, %s, %s)
        """, (
            cliente_id,
            funcionario_id,
            forma_pagamento
        ))

        return cursor.lastrowid


def consultar_venda_completa(id_venda):
    with obter_cursor() as cursor:
        cursor.execute("""
            SELECT
                v.id_venda,
                v.data_venda,
                c.nome AS cliente,
                f.nome AS funcionario,
                v.forma_pagamento,
                p.nome AS produto,
                iv.quantidade,
                iv.preco_unitario,
                (iv.quantidade * iv.preco_unitario) AS subtotal
            FROM vendas v
            JOIN clientes c
                ON c.id_cliente = v.cliente_id
            JOIN funcionarios f
                ON f.id_funcionario = v.funcionario_id
            JOIN itens_venda iv
                ON iv.venda_id = v.id_venda
            JOIN produtos p
                ON p.id_produto = iv.produto_id
            WHERE v.id_venda = %s
            ORDER BY iv.id_item
        """, (id_venda,))

        return cursor.fetchall()
