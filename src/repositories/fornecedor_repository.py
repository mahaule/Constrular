from src.config.database import obter_cursor


def listar_fornecedores():
    with obter_cursor() as cursor:
        cursor.execute("""
            SELECT
                id_fornecedor,
                nome,
                telefone,
                email,
                cidade,
                estado
            FROM fornecedores
            ORDER BY id_fornecedor
        """)

        return cursor.fetchall()


def cadastrar_fornecedor(
    nome,
    telefone,
    email,
    cidade,
    estado
):
    with obter_cursor(commit=True) as cursor:
        cursor.execute("""
            INSERT INTO fornecedores (
                nome,
                telefone,
                email,
                cidade,
                estado
            )
            VALUES (%s, %s, %s, %s, %s)
        """, (
            nome,
            telefone,
            email,
            cidade,
            estado
        ))

        return cursor.lastrowid


def buscar_fornecedor_por_id(id_fornecedor):
    with obter_cursor() as cursor:
        cursor.execute("""
            SELECT
                id_fornecedor,
                nome,
                telefone,
                email,
                cidade,
                estado
            FROM fornecedores
            WHERE id_fornecedor = %s
        """, (id_fornecedor,))

        return cursor.fetchone()


def atualizar_fornecedor(
    id_fornecedor,
    nome,
    telefone,
    email,
    cidade,
    estado
):
    with obter_cursor(commit=True) as cursor:
        cursor.execute("""
            UPDATE fornecedores
            SET
                nome = %s,
                telefone = %s,
                email = %s,
                cidade = %s,
                estado = %s
            WHERE id_fornecedor = %s
        """, (
            nome,
            telefone,
            email,
            cidade,
            estado,
            id_fornecedor
        ))


def excluir_fornecedor(id_fornecedor):
    with obter_cursor(commit=True) as cursor:
        cursor.execute("""
            DELETE FROM fornecedores
            WHERE id_fornecedor = %s
        """, (id_fornecedor,))
