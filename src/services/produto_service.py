from src.repositories.produto_repository import (
    listar_produtos,
    cadastrar_produto,
    listar_categorias,
    listar_fornecedores,
    buscar_produto_por_id,
    atualizar_produto,
    excluir_produto,
    categoria_existe
)

from src.repositories.fornecedor_repository import (
    buscar_fornecedor_por_id
)


def validar_produto(
    nome,
    preco_custo,
    preco_venda,
    estoque_minimo,
    categoria_id,
    fornecedor_id
):
    """
    Valida os dados de um produto antes de
    persistir no banco. Lança ValueError caso
    algum dado esteja inconsistente.
    """
    if not nome or not nome.strip():
        raise ValueError("O nome do produto é obrigatório.")

    if preco_custo is None or preco_venda is None:
        raise ValueError(
            "Preço de custo e preço de venda são obrigatórios."
        )

    if preco_custo < 0:
        raise ValueError(
            "O preço de custo não pode ser negativo."
        )

    if preco_venda < 0:
        raise ValueError(
            "O preço de venda não pode ser negativo."
        )

    if preco_venda < preco_custo:
        raise ValueError(
            "O preço de venda não pode ser menor que "
            "o preço de custo."
        )

    if estoque_minimo is not None and estoque_minimo < 0:
        raise ValueError(
            "O estoque mínimo não pode ser negativo."
        )

    if categoria_id is not None and not categoria_existe(categoria_id):
        raise ValueError(
            f"Categoria com id {categoria_id} não existe."
        )

    if fornecedor_id is not None and not buscar_fornecedor_por_id(fornecedor_id):
        raise ValueError(
            f"Fornecedor com id {fornecedor_id} não existe."
        )


def obter_produtos():
    return listar_produtos()


def criar_produto(
    nome,
    descricao,
    preco_custo,
    preco_venda,
    estoque_minimo,
    categoria_id,
    fornecedor_id
):
    validar_produto(
        nome,
        preco_custo,
        preco_venda,
        estoque_minimo,
        categoria_id,
        fornecedor_id
    )

    cadastrar_produto(
        nome,
        descricao,
        preco_custo,
        preco_venda,
        estoque_minimo,
        categoria_id,
        fornecedor_id
    )


def obter_categorias():
    return listar_categorias()


def obter_fornecedores():
    return listar_fornecedores()


def obter_produto_por_id(id_produto):
    return buscar_produto_por_id(id_produto)


def editar_produto(
    id_produto,
    nome,
    descricao,
    preco_custo,
    preco_venda,
    estoque_minimo,
    categoria_id,
    fornecedor_id
):
    validar_produto(
        nome,
        preco_custo,
        preco_venda,
        estoque_minimo,
        categoria_id,
        fornecedor_id
    )

    atualizar_produto(
        id_produto,
        nome,
        descricao,
        preco_custo,
        preco_venda,
        estoque_minimo,
        categoria_id,
        fornecedor_id
    )


def remover_produto(id_produto):
    excluir_produto(id_produto)
