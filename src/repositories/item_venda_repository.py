from src.config.database import obter_cursor


def listar_itens_venda(id_venda):
    with obter_cursor() as cursor:
        cursor.execute("""
            SELECT
                id_item,
                venda_id,
                produto_id,
                quantidade,
                preco_unitario
            FROM itens_venda
            WHERE venda_id = %s
            ORDER BY id_item
        """, (id_venda,))

        return cursor.fetchall()


def cadastrar_item_venda(
    venda_id,
    produto_id,
    quantidade,
    preco_unitario
):
    with obter_cursor(commit=True) as cursor:
        cursor.execute("""
            INSERT INTO itens_venda (
                venda_id,
                produto_id,
                quantidade,
                preco_unitario
            )
            VALUES (%s, %s, %s, %s)
        """, (
            venda_id,
            produto_id,
            quantidade,
            preco_unitario
        ))

        return cursor.lastrowid
