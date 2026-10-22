from src.repositories.venda_repository import (
    listar_vendas,
    buscar_venda_por_id,
    cadastrar_venda,
    consultar_venda_completa
)

from src.repositories.item_venda_repository import (
    listar_itens_venda,
    cadastrar_item_venda
)

from src.repositories.cliente_repository import (
    buscar_cliente_por_id
)

from src.repositories.funcionario_repository import (
    buscar_funcionario_por_id
)

from src.repositories.produto_repository import (
    buscar_produto_por_id
)

from src.services.estoque_service import (
    obter_estoque,
    registrar_saida
)


def obter_vendas():
    return listar_vendas()


def obter_venda_por_id(id_venda):
    return buscar_venda_por_id(id_venda)


def criar_venda(
    cliente_id,
    funcionario_id,
    forma_pagamento
):
    if not forma_pagamento or not forma_pagamento.strip():
        raise ValueError(
            "A forma de pagamento é obrigatória."
        )

    if not buscar_cliente_por_id(cliente_id):
        raise ValueError(
            f"Cliente com id {cliente_id} não existe."
        )

    if not buscar_funcionario_por_id(funcionario_id):
        raise ValueError(
            f"Funcionário com id {funcionario_id} não existe."
        )

    return cadastrar_venda(
        cliente_id,
        funcionario_id,
        forma_pagamento
    )


def obter_itens_venda(id_venda):
    return listar_itens_venda(id_venda)


def adicionar_item_venda(
    venda_id,
    produto_id,
    quantidade,
    preco_unitario
):
    if quantidade is None or quantidade <= 0:
        raise ValueError(
            "A quantidade do item deve ser maior que zero."
        )

    if preco_unitario is None or preco_unitario < 0:
        raise ValueError(
            "O preço unitário não pode ser negativo."
        )

    if not buscar_produto_por_id(produto_id):
        raise ValueError(
            f"Produto com id {produto_id} não existe."
        )

    cadastrar_item_venda(
        venda_id,
        produto_id,
        quantidade,
        preco_unitario
    )


def obter_venda_completa(id_venda):
    return consultar_venda_completa(id_venda)


def finalizar_venda(id_venda):
    itens = obter_itens_venda(id_venda)

    if not itens:
        raise ValueError(
            "A venda não possui itens."
        )

    # Verifica o estoque de todos os produtos
    for item in itens:
        produto_id = item[2]
        quantidade = item[3]

        estoque_atual = obter_estoque(produto_id)

        if quantidade > estoque_atual:
            raise ValueError(
                f"Estoque insuficiente para o produto "
                f"{produto_id}. "
                f"Disponível: {estoque_atual} | "
                f"Solicitado: {quantidade}"
            )

    # Registra a saída dos produtos
    for item in itens:
        produto_id = item[2]
        quantidade = item[3]

        registrar_saida(
            produto_id,
            quantidade,
            f"Venda #{id_venda}"
        )

    return True
