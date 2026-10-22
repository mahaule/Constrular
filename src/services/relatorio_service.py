from src.repositories.relatorio_repository import (
    consultar_total_vendas,
    consultar_produtos_mais_vendidos,
    consultar_estoque_baixo,
    consultar_faturamento_total
)


def obter_total_vendas():
    return consultar_total_vendas()


def obter_produtos_mais_vendidos():
    return consultar_produtos_mais_vendidos()


def obter_estoque_baixo():
    return consultar_estoque_baixo()


def obter_faturamento_total():
    return consultar_faturamento_total()