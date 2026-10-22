from src.services.venda_service import criar_venda


id_venda = criar_venda(
    cliente_id=6,
    funcionario_id=1,
    forma_pagamento="PIX"
)

print(f"Venda criada com sucesso! ID: {id_venda}")