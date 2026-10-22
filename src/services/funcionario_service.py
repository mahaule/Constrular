from src.repositories.funcionario_repository import (
    listar_funcionarios,
    cadastrar_funcionario,
    buscar_funcionario_por_id,
    atualizar_funcionario,
    excluir_funcionario
)


def validar_funcionario(nome, cargo, salario):
    """
    Valida os dados de um funcionário antes de
    persistir no banco. Lança ValueError caso
    algum dado esteja inconsistente.
    """
    if not nome or not nome.strip():
        raise ValueError("O nome do funcionário é obrigatório.")

    if not cargo or not cargo.strip():
        raise ValueError("O cargo do funcionário é obrigatório.")

    if salario is None:
        raise ValueError("O salário é obrigatório.")

    if salario < 0:
        raise ValueError(
            "O salário não pode ser negativo."
        )

    if salario == 0:
        raise ValueError(
            "O salário deve ser maior que zero."
        )


def obter_funcionarios():
    return listar_funcionarios()


def criar_funcionario(
    nome,
    cargo,
    salario,
    telefone
):
    validar_funcionario(nome, cargo, salario)

    cadastrar_funcionario(
        nome,
        cargo,
        salario,
        telefone
    )


def obter_funcionario_por_id(id_funcionario):
    return buscar_funcionario_por_id(id_funcionario)


def editar_funcionario(
    id_funcionario,
    nome,
    cargo,
    salario,
    telefone
):
    validar_funcionario(nome, cargo, salario)

    atualizar_funcionario(
        id_funcionario,
        nome,
        cargo,
        salario,
        telefone
    )


def remover_funcionario(id_funcionario):
    excluir_funcionario(id_funcionario)
