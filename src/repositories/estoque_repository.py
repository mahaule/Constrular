from src.config.database import obter_cursor


def registrar_movimentacao(
    produto_id,
    tipo,
    quantidade,
    observacao
):
    with obter_cursor(commit=True) as cursor:
        cursor.execute("""
            INSERT INTO movimentacoes_estoque (
                produto_id,
                tipo,
                quantidade,
                data_movimentacao,
                observacao
            )
            VALUES (
                %s,
                %s,
                %s,
                NOW(),
                %s
            )
        """, (
            produto_id,
            tipo,
            quantidade,
            observacao
        ))


def consultar_estoque_produto(produto_id):
    with obter_cursor() as cursor:
        cursor.execute("""
            SELECT
                COALESCE(
                    SUM(
                        CASE
                            WHEN tipo = 'ENTRADA'
                            THEN quantidade
                            WHEN tipo = 'SAIDA'
                            THEN -quantidade
                            ELSE 0
                        END
                    ),
                    0
                )
            FROM movimentacoes_estoque
            WHERE produto_id = %s
        """, (produto_id,))

        return cursor.fetchone()[0]
