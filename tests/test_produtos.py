from src.services.produto_service import (
    obter_produtos,
    criar_produto,
    obter_categorias,
    obter_fornecedores
)


print("Produtos cadastrados:")
for produto in obter_produtos():
    print(produto)

print("\nCategorias disponíveis:")
for categoria in obter_categorias():
    print(categoria)

print("\nFornecedores disponíveis:")
for fornecedor in obter_fornecedores():
    print(fornecedor)

print("\nCadastrando um novo produto de teste...")
criar_produto(
    nome="Produto de Teste",
    descricao="Criado pelo script de teste manual",
    preco_custo=10.00,
    preco_venda=19.90,
    estoque_minimo=5,
    categoria_id=1,
    fornecedor_id=1
)
print("Produto de teste cadastrado com sucesso!")
