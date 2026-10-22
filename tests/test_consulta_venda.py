from src.services.venda_service import obter_venda_completa


venda = obter_venda_completa(5)

for item in venda:
    print(
        f"Venda: {item[0]} | "
        f"Data: {item[1]} | "
        f"Cliente: {item[2]} | "
        f"Funcionário: {item[3]} | "
        f"Pagamento: {item[4]} | "
        f"Produto: {item[5]} | "
        f"Quantidade: {item[6]} | "
        f"Preço: R$ {item[7]:.2f} | "
        f"Subtotal: R$ {item[8]:.2f}"
    )