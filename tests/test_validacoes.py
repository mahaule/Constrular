"""
Testes automatizados das regras de validação da camada de serviços.

Diferente dos scripts em `test_estoque.py`, `test_vendas.py`, etc.
(que são demonstrações manuais e exigem um banco MySQL configurado),
estes testes usam `monkeypatch` para substituir as chamadas ao banco
por valores fixos, então rodam em qualquer máquina, sem precisar de
conexão com o MySQL — inclusive em CI.

Como executar:

    pip install -r requirements-dev.txt
    pytest tests/test_validacoes.py -v
"""

import pytest

from src.services import (
    funcionario_service,
    produto_service,
    cliente_service,
    fornecedor_service,
    estoque_service,
    venda_service,
)


# =============================================================
# FUNCIONÁRIO — salário não pode ser negativo nem zero
# =============================================================

def test_funcionario_salario_negativo_levanta_erro():
    with pytest.raises(ValueError, match="salário não pode ser negativo"):
        funcionario_service.validar_funcionario(
            "João", "Vendedor", -100.0
        )


def test_funcionario_salario_zero_levanta_erro():
    with pytest.raises(ValueError, match="maior que zero"):
        funcionario_service.validar_funcionario(
            "João", "Vendedor", 0
        )


def test_funcionario_nome_vazio_levanta_erro():
    with pytest.raises(ValueError, match="nome"):
        funcionario_service.validar_funcionario(
            "", "Vendedor", 2500.0
        )


def test_funcionario_cargo_vazio_levanta_erro():
    with pytest.raises(ValueError, match="cargo"):
        funcionario_service.validar_funcionario(
            "João", "  ", 2500.0
        )


def test_funcionario_dados_validos_nao_levanta_erro():
    # Não deve levantar nenhuma exceção
    funcionario_service.validar_funcionario("João", "Vendedor", 2500.0)


# =============================================================
# PRODUTO — preços e existência de categoria/fornecedor
# =============================================================

@pytest.fixture
def mock_categoria_e_fornecedor_existentes(monkeypatch):
    """Simula que qualquer categoria/fornecedor informado existe."""
    monkeypatch.setattr(
        produto_service, "categoria_existe", lambda categoria_id: True
    )
    monkeypatch.setattr(
        produto_service,
        "buscar_fornecedor_por_id",
        lambda fornecedor_id: (fornecedor_id, "Fornecedor Teste"),
    )


def test_produto_preco_custo_negativo_levanta_erro(
    mock_categoria_e_fornecedor_existentes
):
    with pytest.raises(ValueError, match="preço de custo"):
        produto_service.validar_produto(
            "Produto", -10, 20, 5, categoria_id=1, fornecedor_id=1
        )


def test_produto_preco_venda_negativo_levanta_erro(
    mock_categoria_e_fornecedor_existentes
):
    with pytest.raises(ValueError, match="preço de venda"):
        produto_service.validar_produto(
            "Produto", 10, -20, 5, categoria_id=1, fornecedor_id=1
        )


def test_produto_venda_menor_que_custo_levanta_erro(
    mock_categoria_e_fornecedor_existentes
):
    with pytest.raises(ValueError, match="menor que"):
        produto_service.validar_produto(
            "Produto", 50, 20, 5, categoria_id=1, fornecedor_id=1
        )


def test_produto_estoque_minimo_negativo_levanta_erro(
    mock_categoria_e_fornecedor_existentes
):
    with pytest.raises(ValueError, match="estoque mínimo"):
        produto_service.validar_produto(
            "Produto", 10, 20, -5, categoria_id=1, fornecedor_id=1
        )


def test_produto_categoria_inexistente_levanta_erro(monkeypatch):
    monkeypatch.setattr(
        produto_service, "categoria_existe", lambda categoria_id: False
    )

    with pytest.raises(ValueError, match="Categoria"):
        produto_service.validar_produto(
            "Produto", 10, 20, 5, categoria_id=999, fornecedor_id=None
        )


def test_produto_fornecedor_inexistente_levanta_erro(monkeypatch):
    monkeypatch.setattr(
        produto_service, "categoria_existe", lambda categoria_id: True
    )
    monkeypatch.setattr(
        produto_service, "buscar_fornecedor_por_id", lambda fornecedor_id: None
    )

    with pytest.raises(ValueError, match="Fornecedor"):
        produto_service.validar_produto(
            "Produto", 10, 20, 5, categoria_id=1, fornecedor_id=999
        )


def test_produto_dados_validos_nao_levanta_erro(
    mock_categoria_e_fornecedor_existentes
):
    produto_service.validar_produto(
        "Produto", 10, 20, 5, categoria_id=1, fornecedor_id=1
    )


# =============================================================
# CLIENTE / FORNECEDOR — nome obrigatório, estado com 2 letras
# =============================================================

def test_cliente_nome_vazio_levanta_erro():
    with pytest.raises(ValueError, match="nome"):
        cliente_service.validar_cliente("", "SP")


def test_cliente_estado_invalido_levanta_erro():
    with pytest.raises(ValueError, match="sigla"):
        cliente_service.validar_cliente("Maria", "São Paulo")


def test_cliente_dados_validos_nao_levanta_erro():
    cliente_service.validar_cliente("Maria", "SP")


def test_fornecedor_nome_vazio_levanta_erro():
    with pytest.raises(ValueError, match="nome"):
        fornecedor_service.validar_fornecedor("", "SP")


def test_fornecedor_dados_validos_nao_levanta_erro():
    fornecedor_service.validar_fornecedor("Distribuidora XYZ", "SP")


# =============================================================
# ESTOQUE — quantidade deve ser positiva; saída não pode
# ultrapassar o estoque disponível
# =============================================================

def test_estoque_entrada_quantidade_zero_levanta_erro():
    with pytest.raises(ValueError, match="maior que zero"):
        estoque_service.registrar_entrada(
            produto_id=1, quantidade=0, observacao="teste"
        )


def test_estoque_saida_quantidade_negativa_levanta_erro():
    with pytest.raises(ValueError, match="maior que zero"):
        estoque_service.registrar_saida(
            produto_id=1, quantidade=-5, observacao="teste"
        )


def test_estoque_saida_maior_que_disponivel_levanta_erro(monkeypatch):
    monkeypatch.setattr(
        estoque_service, "consultar_estoque_produto", lambda produto_id: 3
    )

    with pytest.raises(ValueError, match="insuficiente"):
        estoque_service.registrar_saida(
            produto_id=1, quantidade=10, observacao="teste"
        )


def test_estoque_saida_dentro_do_disponivel_nao_levanta_erro(monkeypatch):
    chamadas = {}

    monkeypatch.setattr(
        estoque_service, "consultar_estoque_produto", lambda produto_id: 100
    )
    monkeypatch.setattr(
        estoque_service,
        "registrar_movimentacao",
        lambda *args, **kwargs: chamadas.setdefault("registrada", True),
    )

    estoque_service.registrar_saida(
        produto_id=1, quantidade=10, observacao="teste"
    )

    assert chamadas.get("registrada") is True


# =============================================================
# VENDA — forma de pagamento obrigatória, cliente/funcionário/
# produto precisam existir, quantidade e preço válidos
# =============================================================

def test_venda_forma_pagamento_vazia_levanta_erro():
    with pytest.raises(ValueError, match="forma de pagamento"):
        venda_service.criar_venda(
            cliente_id=1, funcionario_id=1, forma_pagamento=""
        )


def test_venda_cliente_inexistente_levanta_erro(monkeypatch):
    monkeypatch.setattr(
        venda_service, "buscar_cliente_por_id", lambda cliente_id: None
    )

    with pytest.raises(ValueError, match="Cliente"):
        venda_service.criar_venda(
            cliente_id=999, funcionario_id=1, forma_pagamento="PIX"
        )


def test_venda_funcionario_inexistente_levanta_erro(monkeypatch):
    monkeypatch.setattr(
        venda_service, "buscar_cliente_por_id", lambda cliente_id: (1, "C")
    )
    monkeypatch.setattr(
        venda_service, "buscar_funcionario_por_id", lambda funcionario_id: None
    )

    with pytest.raises(ValueError, match="Funcionário"):
        venda_service.criar_venda(
            cliente_id=1, funcionario_id=999, forma_pagamento="PIX"
        )


def test_venda_dados_validos_retorna_id(monkeypatch):
    monkeypatch.setattr(
        venda_service, "buscar_cliente_por_id", lambda cliente_id: (1, "C")
    )
    monkeypatch.setattr(
        venda_service,
        "buscar_funcionario_por_id",
        lambda funcionario_id: (1, "F"),
    )
    monkeypatch.setattr(
        venda_service, "cadastrar_venda", lambda *args, **kwargs: 42
    )

    venda_id = venda_service.criar_venda(
        cliente_id=1, funcionario_id=1, forma_pagamento="PIX"
    )

    assert venda_id == 42


def test_item_venda_quantidade_zero_levanta_erro():
    with pytest.raises(ValueError, match="quantidade"):
        venda_service.adicionar_item_venda(
            venda_id=1, produto_id=1, quantidade=0, preco_unitario=10.0
        )


def test_item_venda_preco_negativo_levanta_erro():
    with pytest.raises(ValueError, match="preço unitário"):
        venda_service.adicionar_item_venda(
            venda_id=1, produto_id=1, quantidade=1, preco_unitario=-5.0
        )


def test_item_venda_produto_inexistente_levanta_erro(monkeypatch):
    monkeypatch.setattr(
        venda_service, "buscar_produto_por_id", lambda produto_id: None
    )

    with pytest.raises(ValueError, match="Produto"):
        venda_service.adicionar_item_venda(
            venda_id=1, produto_id=999, quantidade=1, preco_unitario=10.0
        )


def test_item_venda_dados_validos_nao_levanta_erro(monkeypatch):
    monkeypatch.setattr(
        venda_service, "buscar_produto_por_id", lambda produto_id: (1, "P")
    )
    monkeypatch.setattr(
        venda_service, "cadastrar_item_venda", lambda *args, **kwargs: None
    )

    venda_service.adicionar_item_venda(
        venda_id=1, produto_id=1, quantidade=2, preco_unitario=10.0
    )
