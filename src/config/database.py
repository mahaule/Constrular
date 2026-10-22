import os
from contextlib import contextmanager

import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def conectar():
    """
    Abre e retorna uma conexão com o banco, lendo as credenciais
    do arquivo .env. Lança um erro claro se alguma variável
    obrigatória não estiver configurada.
    """
    variaveis_obrigatorias = [
        "DB_HOST", "DB_PORT", "DB_USER", "DB_PASSWORD", "DB_NAME"
    ]
    faltando = [v for v in variaveis_obrigatorias if not os.getenv(v)]

    if faltando:
        raise RuntimeError(
            "Variáveis de ambiente ausentes no .env: "
            f"{', '.join(faltando)}. "
            "Copie o .env.example para .env e preencha os valores."
        )

    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )


@contextmanager
def obter_cursor(commit=False):
    """
    Context manager que abre uma conexão e um cursor, garante o
    fechamento de ambos ao final (mesmo se ocorrer um erro) e,
    opcionalmente, faz commit/rollback automático.

    Uso típico em um repository:

        def listar_clientes():
            with obter_cursor() as cursor:
                cursor.execute("SELECT ...")
                return cursor.fetchall()

        def cadastrar_cliente(...):
            with obter_cursor(commit=True) as cursor:
                cursor.execute("INSERT ...", (...))
                return cursor.lastrowid
    """
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        yield cursor

        if commit:
            conexao.commit()

    except Exception:
        if commit:
            conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()
