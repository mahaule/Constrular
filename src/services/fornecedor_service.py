from src.repositories.fornecedor_repository import (
    listar_fornecedores,
    cadastrar_fornecedor,
    buscar_fornecedor_por_id,
    atualizar_fornecedor,
    excluir_fornecedor
)


def validar_fornecedor(nome, estado):
    if not nome or not nome.strip():
        raise ValueError("O nome do fornecedor é obrigatório.")

    if estado and len(estado.strip()) != 2:
        raise ValueError(
            "O estado deve ser informado com a sigla "
            "de 2 letras (ex: SP)."
        )


def obter_fornecedores():
    return listar_fornecedores()


def criar_fornecedor(
    nome,
    telefone,
    email,
    cidade,
    estado
):
    validar_fornecedor(nome, estado)

    cadastrar_fornecedor(
        nome,
        telefone,
        email,
        cidade,
        estado
    )


def obter_fornecedor_por_id(id_fornecedor):
    return buscar_fornecedor_por_id(id_fornecedor)


def editar_fornecedor(
    id_fornecedor,
    nome,
    telefone,
    email,
    cidade,
    estado
):
    validar_fornecedor(nome, estado)

    atualizar_fornecedor(
        id_fornecedor,
        nome,
        telefone,
        email,
        cidade,
        estado
    )


def remover_fornecedor(id_fornecedor):
    excluir_fornecedor(id_fornecedor)
