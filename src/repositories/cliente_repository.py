from src.config.database import obter_cursor


def listar_clientes():
    with obter_cursor() as cursor:
        cursor.execute("""
            SELECT
                id_cliente,
                nome,
                cpf,
                telefone,
                email,
                cidade,
                estado
            FROM clientes
            ORDER BY id_cliente
        """)

        return cursor.fetchall()


def cadastrar_cliente(
    nome,
    cpf,
    telefone,
    email,
    cidade,
    estado
):
    with obter_cursor(commit=True) as cursor:
        cursor.execute("""
            INSERT INTO clientes (
                nome,
                cpf,
                telefone,
                email,
                cidade,
                estado
            )
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            nome,
            cpf,
            telefone,
            email,
            cidade,
            estado
        ))

        return cursor.lastrowid


def buscar_cliente_por_id(id_cliente):
    with obter_cursor() as cursor:
        cursor.execute("""
            SELECT
                id_cliente,
                nome,
                cpf,
                telefone,
                email,
                cidade,
                estado
            FROM clientes
            WHERE id_cliente = %s
        """, (id_cliente,))

        return cursor.fetchone()


def atualizar_cliente(
    id_cliente,
    nome,
    cpf,
    telefone,
    email,
    cidade,
    estado
):
    with obter_cursor(commit=True) as cursor:
        cursor.execute("""
            UPDATE clientes
            SET
                nome = %s,
                cpf = %s,
                telefone = %s,
                email = %s,
                cidade = %s,
                estado = %s
            WHERE id_cliente = %s
        """, (
            nome,
            cpf,
            telefone,
            email,
            cidade,
            estado,
            id_cliente
        ))


def excluir_cliente(id_cliente):
    with obter_cursor(commit=True) as cursor:
        cursor.execute("""
            DELETE FROM clientes
            WHERE id_cliente = %s
        """, (id_cliente,))
