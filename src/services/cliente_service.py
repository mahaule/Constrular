from src.repositories.cliente_repository import (
    listar_clientes,
    cadastrar_cliente,
    buscar_cliente_por_id,
    atualizar_cliente,
    excluir_cliente
)


def validar_cliente(nome, estado):
    if not nome or not nome.strip():
        raise ValueError("O nome do cliente é obrigatório.")

    if estado and len(estado.strip()) != 2:
        raise ValueError(
            "O estado deve ser informado com a sigla "
            "de 2 letras (ex: SP)."
        )


def obter_clientes():
    return listar_clientes()


def criar_cliente(
    nome,
    cpf,
    telefone,
    email,
    cidade,
    estado
):
    validar_cliente(nome, estado)

    cadastrar_cliente(
        nome,
        cpf,
        telefone,
        email,
        cidade,
        estado
    )


def obter_cliente_por_id(id_cliente):
    return buscar_cliente_por_id(id_cliente)


def editar_cliente(
    id_cliente,
    nome,
    cpf,
    telefone,
    email,
    cidade,
    estado
):
    validar_cliente(nome, estado)

    atualizar_cliente(
        id_cliente,
        nome,
        cpf,
        telefone,
        email,
        cidade,
        estado
    )


def remover_cliente(id_cliente):
    excluir_cliente(id_cliente)
