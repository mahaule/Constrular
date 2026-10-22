from src.services.estoque_service import (
    registrar_entrada,
    registrar_saida,
    obter_estoque
)


produto_id = 1


print("Estoque inicial:")
print(obter_estoque(produto_id))


print("\nRegistrando entrada de 10 unidades...")
registrar_entrada(
    produto_id,
    10,
    "Entrada para teste"
)


print("Estoque após entrada:")
print(obter_estoque(produto_id))


print("\nRegistrando saída de 2 unidades...")
registrar_saida(
    produto_id,
    2,
    "Saída para teste"
)


print("Estoque após saída:")
print(obter_estoque(produto_id))