from src.repositories.estoque_repository import (
    registrar_movimentacao,
    consultar_estoque_produto
)


def registrar_entrada(
    produto_id,
    quantidade,
    observacao
):
    if quantidade is None or quantidade <= 0:
        raise ValueError(
            "A quantidade de entrada deve ser maior que zero."
        )

    registrar_movimentacao(
        produto_id,
        "ENTRADA",
        quantidade,
        observacao
    )


def registrar_saida(
    produto_id,
    quantidade,
    observacao
):
    if quantidade is None or quantidade <= 0:
        raise ValueError(
            "A quantidade de saída deve ser maior que zero."
        )

    estoque_atual = consultar_estoque_produto(produto_id)

    if quantidade > estoque_atual:
        raise ValueError(
            f"Estoque insuficiente. "
            f"Estoque atual: {estoque_atual}"
        )

    registrar_movimentacao(
        produto_id,
        "SAIDA",
        quantidade,
        observacao
    )


def obter_estoque(produto_id):
    return consultar_estoque_produto(produto_id)
