from src.config.database import obter_cursor


def listar_funcionarios():
    with obter_cursor() as cursor:
        cursor.execute("""
            SELECT
                id_funcionario,
                nome,
                cargo,
                salario,
                telefone
            FROM funcionarios
            ORDER BY id_funcionario
        """)

        return cursor.fetchall()


def cadastrar_funcionario(
    nome,
    cargo,
    salario,
    telefone
):
    with obter_cursor(commit=True) as cursor:
        cursor.execute("""
            INSERT INTO funcionarios (
                nome,
                cargo,
                salario,
                telefone
            )
            VALUES (%s, %s, %s, %s)
        """, (
            nome,
            cargo,
            salario,
            telefone
        ))

        return cursor.lastrowid


def buscar_funcionario_por_id(id_funcionario):
    with obter_cursor() as cursor:
        cursor.execute("""
            SELECT
                id_funcionario,
                nome,
                cargo,
                salario,
                telefone
            FROM funcionarios
            WHERE id_funcionario = %s
        """, (id_funcionario,))

        return cursor.fetchone()


def atualizar_funcionario(
    id_funcionario,
    nome,
    cargo,
    salario,
    telefone
):
    with obter_cursor(commit=True) as cursor:
        cursor.execute("""
            UPDATE funcionarios
            SET
                nome = %s,
                cargo = %s,
                salario = %s,
                telefone = %s
            WHERE id_funcionario = %s
        """, (
            nome,
            cargo,
            salario,
            telefone,
            id_funcionario
        ))


def excluir_funcionario(id_funcionario):
    with obter_cursor(commit=True) as cursor:
        cursor.execute("""
            DELETE FROM funcionarios
            WHERE id_funcionario = %s
        """, (id_funcionario,))
