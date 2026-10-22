from src.services.venda_service import adicionar_item_venda


adicionar_item_venda(
    venda_id=5,
    produto_id=1,
    quantidade=2,
    preco_unitario=38.00
)

print("Item adicionado com sucesso!")