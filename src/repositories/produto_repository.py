from src.config.database import obter_cursor


def listar_produtos():
    with obter_cursor() as cursor:
        cursor.execute("""
            SELECT
                id_produto,
                nome,
                preco_custo,
                preco_venda,
                estoque_minimo
            FROM produtos
            ORDER BY id_produto
        """)

        return cursor.fetchall()


def cadastrar_produto(
    nome,
    descricao,
    preco_custo,
    preco_venda,
    estoque_minimo,
    categoria_id,
    fornecedor_id
):
    with obter_cursor(commit=True) as cursor:
        cursor.execute("""
            INSERT INTO produtos (
                nome,
                descricao,
                preco_custo,
                preco_venda,
                estoque_minimo,
                categoria_id,
                fornecedor_id
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            nome,
            descricao,
            preco_custo,
            preco_venda,
            estoque_minimo,
            categoria_id,
            fornecedor_id
        ))

        return cursor.lastrowid


def listar_categorias():
    with obter_cursor() as cursor:
        cursor.execute("""
            SELECT
                id_categoria,
                nome
            FROM categorias
            ORDER BY id_categoria
        """)

        return cursor.fetchall()


def categoria_existe(categoria_id):
    with obter_cursor() as cursor:
        cursor.execute("""
            SELECT 1
            FROM categorias
            WHERE id_categoria = %s
        """, (categoria_id,))

        return cursor.fetchone() is not None


def listar_fornecedores():
    with obter_cursor() as cursor:
        cursor.execute("""
            SELECT
                id_fornecedor,
                nome
            FROM fornecedores
            ORDER BY id_fornecedor
        """)

        return cursor.fetchall()


def buscar_produto_por_id(id_produto):
    with obter_cursor() as cursor:
        cursor.execute("""
            SELECT
                id_produto,
                nome,
                descricao,
                preco_custo,
                preco_venda,
                estoque_minimo,
                categoria_id,
                fornecedor_id
            FROM produtos
            WHERE id_produto = %s
        """, (id_produto,))

        return cursor.fetchone()


def atualizar_produto(
    id_produto,
    nome,
    descricao,
    preco_custo,
    preco_venda,
    estoque_minimo,
    categoria_id,
    fornecedor_id
):
    with obter_cursor(commit=True) as cursor:
        cursor.execute("""
            UPDATE produtos
            SET
                nome = %s,
                descricao = %s,
                preco_custo = %s,
                preco_venda = %s,
                estoque_minimo = %s,
                categoria_id = %s,
                fornecedor_id = %s
            WHERE id_produto = %s
        """, (
            nome,
            descricao,
            preco_custo,
            preco_venda,
            estoque_minimo,
            categoria_id,
            fornecedor_id,
            id_produto
        ))


def excluir_produto(id_produto):
    with obter_cursor(commit=True) as cursor:
        cursor.execute("""
            DELETE FROM produtos
            WHERE id_produto = %s
        """, (id_produto,))
