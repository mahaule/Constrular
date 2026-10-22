
from src.services.relatorio_service import (
    obter_total_vendas,
    obter_produtos_mais_vendidos,
    obter_estoque_baixo,
    obter_faturamento_total
)

from src.services.estoque_service import (
    obter_estoque,
    registrar_entrada,
    registrar_saida
)

from src.services.produto_service import (
    obter_produtos,
    criar_produto,
    obter_categorias,
    obter_fornecedores,
    obter_produto_por_id,
    editar_produto,
    remover_produto
)

from src.services.cliente_service import (
    obter_clientes,
    criar_cliente,
    obter_cliente_por_id,
    editar_cliente,
    remover_cliente
)

from src.services.fornecedor_service import (
    obter_fornecedores as obter_fornecedores_cadastro,
    criar_fornecedor,
    obter_fornecedor_por_id,
    editar_fornecedor,
    remover_fornecedor
)

from src.services.funcionario_service import (
    obter_funcionarios,
    criar_funcionario,
    obter_funcionario_por_id,
    editar_funcionario,
    remover_funcionario
)

from src.services.venda_service import (
    obter_vendas,
    criar_venda,
    adicionar_item_venda,
    obter_venda_completa,
    finalizar_venda
)

def menu():
    while True:
        print("\n" + "=" * 40)
        print("        SISTEMA CONSTRULAR")
        print("=" * 40)
        print("1 - Produtos")
        print("2 - Clientes")
        print("3 - Fornecedores")
        print("4 - Funcionários")
        print("5 - Vendas")
        print("6 - Estoque")
        print("7 - Relatórios")
        print("0 - Sair")
        print("=" * 40)

        opcao = input("Escolha uma opção: ")

        try:
            match opcao:

                # =========================
                # PRODUTOS
                # =========================

                case "1":
                    while True:
                        print("\n--- PRODUTOS ---")
                        print("1 - Listar produtos")
                        print("2 - Cadastrar produto")
                        print("3 - Buscar produto")
                        print("4 - Alterar produto")
                        print("5 - Excluir produto")
                        print("0 - Voltar")

                        opcao_produto = input("Escolha uma opção: ")

                        match opcao_produto:

                            case "1":
                                produtos = obter_produtos()

                                print("\n--- LISTA DE PRODUTOS ---")

                                for produto in produtos:
                                    print(
                                        f"ID: {produto[0]} | "
                                        f"Produto: {produto[1]} | "
                                        f"Custo: R$ {produto[2]:.2f} | "
                                        f"Venda: R$ {produto[3]:.2f} | "
                                        f"Estoque mínimo: {produto[4]}"
                                    )

                            case "2":
                                print("\n--- CADASTRAR PRODUTO ---")

                                nome = input("Nome: ")
                                descricao = input("Descrição: ")
                                preco_custo = float(
                                    input("Preço de custo: ")
                                )
                                preco_venda = float(
                                    input("Preço de venda: ")
                                )
                                estoque_minimo = int(
                                    input("Estoque mínimo: ")
                                )

                                print("\nCategorias:")
                                categorias = obter_categorias()

                                for categoria in categorias:
                                    print(
                                        f"{categoria[0]} - "
                                        f"{categoria[1]}"
                                    )

                                categoria_id = int(
                                    input("Escolha a categoria: ")
                                )

                                print("\nFornecedores:")
                                fornecedores = obter_fornecedores()

                                for fornecedor in fornecedores:
                                    print(
                                        f"{fornecedor[0]} - "
                                        f"{fornecedor[1]}"
                                    )

                                fornecedor_id = int(
                                    input("Escolha o fornecedor: ")
                                )

                                try:
                                    criar_produto(
                                        nome,
                                        descricao,
                                        preco_custo,
                                        preco_venda,
                                        estoque_minimo,
                                        categoria_id,
                                        fornecedor_id
                                    )

                                    print(
                                        "\nProduto cadastrado com sucesso!"
                                    )

                                except ValueError as erro:
                                    print(f"\nErro: {erro}")

                            case "3":
                                print("\n--- BUSCAR PRODUTO ---")

                                id_produto = int(
                                    input("Digite o ID do produto: ")
                                )

                                produto = obter_produto_por_id(
                                    id_produto
                                )

                                if produto:
                                    print("\nProduto encontrado:")
                                    print(f"ID: {produto[0]}")
                                    print(f"Nome: {produto[1]}")
                                    print(f"Descrição: {produto[2]}")
                                    print(
                                        f"Preço de custo: "
                                        f"R$ {produto[3]:.2f}"
                                    )
                                    print(
                                        f"Preço de venda: "
                                        f"R$ {produto[4]:.2f}"
                                    )
                                    print(
                                        f"Estoque mínimo: "
                                        f"{produto[5]}"
                                    )
                                    print(
                                        f"Categoria ID: "
                                        f"{produto[6]}"
                                    )
                                    print(
                                        f"Fornecedor ID: "
                                        f"{produto[7]}"
                                    )
                                else:
                                    print(
                                        "\nProduto não encontrado."
                                    )

                            case "4":
                                print("\n--- ALTERAR PRODUTO ---")

                                id_produto = int(
                                    input("Digite o ID do produto: ")
                                )

                                produto = obter_produto_por_id(
                                    id_produto
                                )

                                if not produto:
                                    print(
                                        "\nProduto não encontrado."
                                    )
                                    continue

                                print("\nDados atuais:")
                                print(f"Nome: {produto[1]}")
                                print(f"Descrição: {produto[2]}")
                                print(
                                    f"Preço de custo: "
                                    f"R$ {produto[3]:.2f}"
                                )
                                print(
                                    f"Preço de venda: "
                                    f"R$ {produto[4]:.2f}"
                                )
                                print(
                                    f"Estoque mínimo: "
                                    f"{produto[5]}"
                                )

                                print("\nDigite os novos dados:")

                                nome = input("Nome: ")
                                descricao = input("Descrição: ")
                                preco_custo = float(
                                    input("Preço de custo: ")
                                )
                                preco_venda = float(
                                    input("Preço de venda: ")
                                )
                                estoque_minimo = int(
                                    input("Estoque mínimo: ")
                                )

                                print("\nCategorias:")
                                categorias = obter_categorias()

                                for categoria in categorias:
                                    print(
                                        f"{categoria[0]} - "
                                        f"{categoria[1]}"
                                    )

                                categoria_id = int(
                                    input("Escolha a categoria: ")
                                )

                                print("\nFornecedores:")
                                fornecedores = obter_fornecedores()

                                for fornecedor in fornecedores:
                                    print(
                                        f"{fornecedor[0]} - "
                                        f"{fornecedor[1]}"
                                    )

                                fornecedor_id = int(
                                    input("Escolha o fornecedor: ")
                                )

                                try:
                                    editar_produto(
                                        id_produto,
                                        nome,
                                        descricao,
                                        preco_custo,
                                        preco_venda,
                                        estoque_minimo,
                                        categoria_id,
                                        fornecedor_id
                                    )

                                    print(
                                        "\nProduto alterado com sucesso!"
                                    )

                                except ValueError as erro:
                                    print(f"\nErro: {erro}")

                            case "5":
                                print("\n--- EXCLUIR PRODUTO ---")

                                id_produto = int(
                                    input("Digite o ID do produto: ")
                                )

                                produto = obter_produto_por_id(
                                    id_produto
                                )

                                if not produto:
                                    print(
                                        "\nProduto não encontrado."
                                    )
                                    continue

                                print(
                                    f"\nProduto: {produto[1]}"
                                )
                                print(
                                    f"Descrição: {produto[2]}"
                                )

                                confirmacao = input(
                                    "\nDeseja realmente excluir "
                                    "este produto? (S/N): "
                                )

                                if confirmacao.upper() == "S":
                                    remover_produto(id_produto)

                                    print(
                                        "\nProduto excluído "
                                        "com sucesso!"
                                    )
                                else:
                                    print(
                                        "\nExclusão cancelada."
                                    )

                            case "0":
                                break

                            case _:
                                print("\nOpção inválida!")

                # =========================
                # CLIENTES
                # =========================

                case "2":
                    while True:
                        print("\n--- CLIENTES ---")
                        print("1 - Listar clientes")
                        print("2 - Cadastrar cliente")
                        print("3 - Buscar cliente")
                        print("4 - Alterar cliente")
                        print("5 - Excluir cliente")
                        print("0 - Voltar")

                        opcao_cliente = input(
                            "Escolha uma opção: "
                        )

                        match opcao_cliente:

                            case "1":
                                clientes = obter_clientes()

                                print("\n--- LISTA DE CLIENTES ---")

                                for cliente in clientes:
                                    print(
                                        f"ID: {cliente[0]} | "
                                        f"Nome: {cliente[1]} | "
                                        f"CPF: {cliente[2]} | "
                                        f"Telefone: {cliente[3]} | "
                                        f"E-mail: {cliente[4]} | "
                                        f"Cidade: {cliente[5]} | "
                                        f"Estado: {cliente[6]}"
                                    )

                            case "2":
                                print("\n--- CADASTRAR CLIENTE ---")

                                nome = input("Nome: ")
                                cpf = input("CPF: ")
                                telefone = input("Telefone: ")
                                email = input("E-mail: ")
                                cidade = input("Cidade: ")
                                estado = input("Estado: ")

                                try:
                                    criar_cliente(
                                        nome,
                                        cpf,
                                        telefone,
                                        email,
                                        cidade,
                                        estado
                                    )

                                    print(
                                        "\nCliente cadastrado com sucesso!"
                                    )

                                except ValueError as erro:
                                    print(f"\nErro: {erro}")

                            case "3":
                                print("\n--- BUSCAR CLIENTE ---")

                                id_cliente = int(
                                    input("Digite o ID do cliente: ")
                                )

                                cliente = obter_cliente_por_id(
                                    id_cliente
                                )

                                if cliente:
                                    print("\nCliente encontrado:")
                                    print(f"ID: {cliente[0]}")
                                    print(f"Nome: {cliente[1]}")
                                    print(f"CPF: {cliente[2]}")
                                    print(
                                        f"Telefone: {cliente[3]}"
                                    )
                                    print(
                                        f"E-mail: {cliente[4]}"
                                    )
                                    print(
                                        f"Cidade: {cliente[5]}"
                                    )
                                    print(
                                        f"Estado: {cliente[6]}"
                                    )
                                else:
                                    print(
                                        "\nCliente não encontrado."
                                    )

                            case "4":
                                print("\n--- ALTERAR CLIENTE ---")

                                id_cliente = int(
                                    input("Digite o ID do cliente: ")
                                )

                                cliente = obter_cliente_por_id(
                                    id_cliente
                                )

                                if not cliente:
                                    print(
                                        "\nCliente não encontrado."
                                    )
                                    continue

                                print("\nDados atuais:")
                                print(f"Nome: {cliente[1]}")
                                print(f"CPF: {cliente[2]}")
                                print(
                                    f"Telefone: {cliente[3]}"
                                )
                                print(
                                    f"E-mail: {cliente[4]}"
                                )
                                print(
                                    f"Cidade: {cliente[5]}"
                                )
                                print(
                                    f"Estado: {cliente[6]}"
                                )

                                print("\nDigite os novos dados:")

                                nome = input("Nome: ")
                                cpf = input("CPF: ")
                                telefone = input("Telefone: ")
                                email = input("E-mail: ")
                                cidade = input("Cidade: ")
                                estado = input("Estado: ")

                                try:
                                    editar_cliente(
                                        id_cliente,
                                        nome,
                                        cpf,
                                        telefone,
                                        email,
                                        cidade,
                                        estado
                                    )

                                    print(
                                        "\nCliente alterado com sucesso!"
                                    )

                                except ValueError as erro:
                                    print(f"\nErro: {erro}")

                            case "5":
                                print("\n--- EXCLUIR CLIENTE ---")

                                id_cliente = int(
                                    input("Digite o ID do cliente: ")
                                )

                                cliente = obter_cliente_por_id(
                                    id_cliente
                                )

                                if not cliente:
                                    print(
                                        "\nCliente não encontrado."
                                    )
                                    continue

                                print(
                                    f"\nCliente: {cliente[1]}"
                                )
                                print(
                                    f"CPF: {cliente[2]}"
                                )

                                confirmacao = input(
                                    "\nDeseja realmente excluir "
                                    "este cliente? (S/N): "
                                )

                                if confirmacao.upper() == "S":
                                    remover_cliente(id_cliente)

                                    print(
                                        "\nCliente excluído "
                                        "com sucesso!"
                                    )
                                else:
                                    print(
                                        "\nExclusão cancelada."
                                    )

                            case "0":
                                break

                            case _:
                                print("\nOpção inválida!")

                # =========================
                # FORNECEDORES
                # =========================

                case "3":
                    while True:
                        print("\n--- FORNECEDORES ---")
                        print("1 - Listar fornecedores")
                        print("2 - Cadastrar fornecedor")
                        print("3 - Buscar fornecedor")
                        print("4 - Alterar fornecedor")
                        print("5 - Excluir fornecedor")
                        print("0 - Voltar")

                        opcao_fornecedor = input(
                            "Escolha uma opção: "
                        )

                        match opcao_fornecedor:

                            case "1":
                                fornecedores = (
                                    obter_fornecedores_cadastro()
                                )

                                print(
                                    "\n--- LISTA DE FORNECEDORES ---"
                                )

                                for fornecedor in fornecedores:
                                    print(
                                        f"ID: {fornecedor[0]} | "
                                        f"Nome: {fornecedor[1]} | "
                                        f"Telefone: {fornecedor[2]} | "
                                        f"E-mail: {fornecedor[3]} | "
                                        f"Cidade: {fornecedor[4]} | "
                                        f"Estado: {fornecedor[5]}"
                                    )

                            case "2":
                                print(
                                    "\n--- CADASTRAR FORNECEDOR ---"
                                )

                                nome = input("Nome: ")
                                telefone = input("Telefone: ")
                                email = input("E-mail: ")
                                cidade = input("Cidade: ")
                                estado = input("Estado: ")

                                try:
                                    criar_fornecedor(
                                        nome,
                                        telefone,
                                        email,
                                        cidade,
                                        estado
                                    )

                                    print(
                                        "\nFornecedor cadastrado "
                                        "com sucesso!"
                                    )

                                except ValueError as erro:
                                    print(f"\nErro: {erro}")

                            case "3":
                                print(
                                    "\n--- BUSCAR FORNECEDOR ---"
                                )

                                id_fornecedor = int(
                                    input(
                                        "Digite o ID do fornecedor: "
                                    )
                                )

                                fornecedor = (
                                    obter_fornecedor_por_id(
                                        id_fornecedor
                                    )
                                )

                                if fornecedor:
                                    print(
                                        "\nFornecedor encontrado:"
                                    )
                                    print(
                                        f"ID: {fornecedor[0]}"
                                    )
                                    print(
                                        f"Nome: {fornecedor[1]}"
                                    )
                                    print(
                                        f"Telefone: {fornecedor[2]}"
                                    )
                                    print(
                                        f"E-mail: {fornecedor[3]}"
                                    )
                                    print(
                                        f"Cidade: {fornecedor[4]}"
                                    )
                                    print(
                                        f"Estado: {fornecedor[5]}"
                                    )
                                else:
                                    print(
                                        "\nFornecedor não encontrado."
                                    )

                            case "4":
                                print(
                                    "\n--- ALTERAR FORNECEDOR ---"
                                )

                                id_fornecedor = int(
                                    input(
                                        "Digite o ID do fornecedor: "
                                    )
                                )

                                fornecedor = (
                                    obter_fornecedor_por_id(
                                        id_fornecedor
                                    )
                                )

                                if not fornecedor:
                                    print(
                                        "\nFornecedor não encontrado."
                                    )
                                    continue

                                print("\nDados atuais:")
                                print(
                                    f"Nome: {fornecedor[1]}"
                                )
                                print(
                                    f"Telefone: {fornecedor[2]}"
                                )
                                print(
                                    f"E-mail: {fornecedor[3]}"
                                )
                                print(
                                    f"Cidade: {fornecedor[4]}"
                                )
                                print(
                                    f"Estado: {fornecedor[5]}"
                                )

                                print(
                                    "\nDigite os novos dados:"
                                )

                                nome = input("Nome: ")
                                telefone = input("Telefone: ")
                                email = input("E-mail: ")
                                cidade = input("Cidade: ")
                                estado = input("Estado: ")

                                try:
                                    editar_fornecedor(
                                        id_fornecedor,
                                        nome,
                                        telefone,
                                        email,
                                        cidade,
                                        estado
                                    )

                                    print(
                                        "\nFornecedor alterado "
                                        "com sucesso!"
                                    )

                                except ValueError as erro:
                                    print(f"\nErro: {erro}")

                            case "5":
                                print(
                                    "\n--- EXCLUIR FORNECEDOR ---"
                                )

                                id_fornecedor = int(
                                    input(
                                        "Digite o ID do fornecedor: "
                                    )
                                )

                                fornecedor = (
                                    obter_fornecedor_por_id(
                                        id_fornecedor
                                    )
                                )

                                if not fornecedor:
                                    print(
                                        "\nFornecedor não encontrado."
                                    )
                                    continue

                                print(
                                    f"\nFornecedor: "
                                    f"{fornecedor[1]}"
                                )
                                print(
                                    f"Telefone: "
                                    f"{fornecedor[2]}"
                                )

                                confirmacao = input(
                                    "\nDeseja realmente excluir "
                                    "este fornecedor? (S/N): "
                                )

                                if confirmacao.upper() == "S":
                                    remover_fornecedor(
                                        id_fornecedor
                                    )

                                    print(
                                        "\nFornecedor excluído "
                                        "com sucesso!"
                                    )
                                else:
                                    print(
                                        "\nExclusão cancelada."
                                    )

                            case "0":
                                break

                            case _:
                                print("\nOpção inválida!")

                # =========================
                # FUNCIONÁRIOS
                # =========================

                case "4":
                    while True:
                        print("\n--- FUNCIONÁRIOS ---")
                        print("1 - Listar funcionários")
                        print("2 - Cadastrar funcionário")
                        print("3 - Buscar funcionário")
                        print("4 - Alterar funcionário")
                        print("5 - Excluir funcionário")
                        print("0 - Voltar")

                        opcao_funcionario = input(
                            "Escolha uma opção: "
                        )

                        match opcao_funcionario:

                            case "1":
                                funcionarios = obter_funcionarios()

                                print(
                                    "\n--- LISTA DE FUNCIONÁRIOS ---"
                                )

                                for funcionario in funcionarios:
                                    print(
                                        f"ID: {funcionario[0]} | "
                                        f"Nome: {funcionario[1]} | "
                                        f"Cargo: {funcionario[2]} | "
                                        f"Salário: "
                                        f"R$ {funcionario[3]:.2f} | "
                                        f"Telefone: {funcionario[4]}"
                                    )

                            case "2":
                                print(
                                    "\n--- CADASTRAR FUNCIONÁRIO ---"
                                )

                                nome = input("Nome: ")
                                cargo = input("Cargo: ")
                                salario = float(
                                    input("Salário: ")
                                )
                                telefone = input("Telefone: ")

                                try:
                                    criar_funcionario(
                                        nome,
                                        cargo,
                                        salario,
                                        telefone
                                    )

                                    print(
                                        "\nFuncionário cadastrado "
                                        "com sucesso!"
                                    )

                                except ValueError as erro:
                                    print(f"\nErro: {erro}")

                            case "3":
                                print(
                                    "\n--- BUSCAR FUNCIONÁRIO ---"
                                )

                                id_funcionario = int(
                                    input(
                                        "Digite o ID do funcionário: "
                                    )
                                )

                                funcionario = (
                                    obter_funcionario_por_id(
                                        id_funcionario
                                    )
                                )

                                if funcionario:
                                    print(
                                        "\nFuncionário encontrado:"
                                    )
                                    print(
                                        f"ID: {funcionario[0]}"
                                    )
                                    print(
                                        f"Nome: {funcionario[1]}"
                                    )
                                    print(
                                        f"Cargo: {funcionario[2]}"
                                    )
                                    print(
                                        f"Salário: "
                                        f"R$ {funcionario[3]:.2f}"
                                    )
                                    print(
                                        f"Telefone: "
                                        f"{funcionario[4]}"
                                    )
                                else:
                                    print(
                                        "\nFuncionário não encontrado."
                                    )

                            case "4":
                                print(
                                    "\n--- ALTERAR FUNCIONÁRIO ---"
                                )

                                id_funcionario = int(
                                    input(
                                        "Digite o ID do funcionário: "
                                    )
                                )

                                funcionario = (
                                    obter_funcionario_por_id(
                                        id_funcionario
                                    )
                                )

                                if not funcionario:
                                    print(
                                        "\nFuncionário não encontrado."
                                    )
                                    continue

                                print("\nDados atuais:")
                                print(
                                    f"Nome: {funcionario[1]}"
                                )
                                print(
                                    f"Cargo: {funcionario[2]}"
                                )
                                print(
                                    f"Salário: "
                                    f"R$ {funcionario[3]:.2f}"
                                )
                                print(
                                    f"Telefone: "
                                    f"{funcionario[4]}"
                                )

                                print(
                                    "\nDigite os novos dados:"
                                )

                                nome = input("Nome: ")
                                cargo = input("Cargo: ")
                                salario = float(
                                    input("Salário: ")
                                )
                                telefone = input("Telefone: ")

                                try:
                                    editar_funcionario(
                                        id_funcionario,
                                        nome,
                                        cargo,
                                        salario,
                                        telefone
                                    )

                                    print(
                                        "\nFuncionário alterado "
                                        "com sucesso!"
                                    )

                                except ValueError as erro:
                                    print(f"\nErro: {erro}")

                            case "5":
                                print(
                                    "\n--- EXCLUIR FUNCIONÁRIO ---"
                                )

                                id_funcionario = int(
                                    input(
                                        "Digite o ID do funcionário: "
                                    )
                                )

                                funcionario = (
                                    obter_funcionario_por_id(
                                        id_funcionario
                                    )
                                )

                                if not funcionario:
                                    print(
                                        "\nFuncionário não encontrado."
                                    )
                                    continue

                                print(
                                    f"\nFuncionário: "
                                    f"{funcionario[1]}"
                                )
                                print(
                                    f"Cargo: "
                                    f"{funcionario[2]}"
                                )

                                confirmacao = input(
                                    "\nDeseja realmente excluir "
                                    "este funcionário? (S/N): "
                                )

                                if confirmacao.upper() == "S":
                                    remover_funcionario(
                                        id_funcionario
                                    )

                                    print(
                                        "\nFuncionário excluído "
                                        "com sucesso!"
                                    )
                                else:
                                    print(
                                        "\nExclusão cancelada."
                                    )

                            case "0":
                                break

                            case _:
                                print("\nOpção inválida!")

                # =========================
                # VENDAS
                # =========================

                case "5":
                    while True:
                        print("\n--- VENDAS ---")
                        print("1 - Listar vendas")
                        print("2 - Consultar venda")
                        print("3 - Finalizar venda")
                        print("4 - Cadastrar venda")
                        print("0 - Voltar")

                        opcao_venda = input("Escolha uma opção: ")

                        match opcao_venda:

                            case "1":
                                vendas = obter_vendas()

                                print("\n--- LISTA DE VENDAS ---")

                                for venda in vendas:
                                    print(
                                        f"ID: {venda[0]} | "
                                        f"Data: {venda[1]} | "
                                        f"Cliente ID: {venda[2]} | "
                                        f"Funcionário ID: {venda[3]} | "
                                        f"Pagamento: {venda[4]}"
                                    )

                            case "2":
                                print("\n--- CONSULTAR VENDA ---")

                                id_venda = int(
                                    input("Digite o ID da venda: ")
                                )

                                venda = obter_venda_completa(id_venda)

                                if venda:
                                    print("\n--- VENDA ---")

                                    total = 0

                                    print(f"Venda: {venda[0][0]}")
                                    print(f"Data: {venda[0][1]}")
                                    print(f"Cliente: {venda[0][2]}")
                                    print(f"Funcionário: {venda[0][3]}")
                                    print(f"Pagamento: {venda[0][4]}")

                                    print("\n--- ITENS ---")

                                    for item in venda:
                                        print(
                                            f"Produto: {item[5]} | "
                                            f"Quantidade: {item[6]} | "
                                            f"Preço: R$ {item[7]:.2f} | "
                                            f"Subtotal: R$ {item[8]:.2f}"
                                        )

                                        total += item[8]

                                    print(f"\nTOTAL: R$ {total:.2f}")

                                else:
                                    print("\nVenda não encontrada.")

                            case "3":
                                print("\n--- FINALIZAR VENDA ---")

                                id_venda = int(
                                    input("Digite o ID da venda: ")
                                )

                                try:
                                    finalizar_venda(id_venda)

                                    print(
                                        "\nVenda finalizada com sucesso!"
                                    )
                                    print("Estoque atualizado.")

                                except ValueError as erro:
                                    print(f"\nErro: {erro}")

                            case "4":
                                print("\n--- CADASTRAR VENDA ---")

                                cliente_id = int(
                                    input("ID do cliente: ")
                                )

                                funcionario_id = int(
                                    input("ID do funcionário: ")
                                )

                                forma_pagamento = input(
                                    "Forma de pagamento: "
                                )

                                try:
                                    id_venda = criar_venda(
                                        cliente_id,
                                        funcionario_id,
                                        forma_pagamento
                                    )
                                except ValueError as erro:
                                    print(f"\nErro: {erro}")
                                    continue

                                print(
                                    f"\nVenda criada com sucesso! "
                                    f"ID: {id_venda}"
                                )

                                while True:
                                    print(
                                        "\n--- ADICIONAR PRODUTO ---"
                                    )

                                    produto_id = int(
                                        input("ID do produto: ")
                                    )

                                    quantidade = int(
                                        input("Quantidade: ")
                                    )

                                    preco_unitario = float(
                                        input("Preço unitário: ")
                                    )

                                    try:
                                        adicionar_item_venda(
                                            id_venda,
                                            produto_id,
                                            quantidade,
                                            preco_unitario
                                        )

                                        print(
                                            "\nProduto adicionado à venda!"
                                        )

                                    except ValueError as erro:
                                        print(f"\nErro: {erro}")

                                    continuar = input(
                                        "\nAdicionar outro produto? (S/N): "
                                    )

                                    if continuar.upper() != "S":
                                        break

                                print(
                                    f"\nVenda #{id_venda} "
                                    f"criada com sucesso!"
                                )

                            case "0":
                                break

                            case _:
                                print("\nOpção inválida!")

                # =========================
                # ESTOQUE
                # =========================

                case "6":
                    while True:
                        print("\n--- ESTOQUE ---")
                        print("1 - Consultar estoque")
                        print("2 - Registrar entrada")
                        print("3 - Registrar saída")
                        print("0 - Voltar")

                        opcao_estoque = input(
                            "Escolha uma opção: "
                        )

                        match opcao_estoque:

                            case "1":
                                print("\n--- CONSULTAR ESTOQUE ---")

                                produto_id = int(
                                    input("ID do produto: ")
                                )

                                estoque = obter_estoque(
                                    produto_id
                                )

                                print(
                                    f"\nEstoque atual: {estoque}"
                                )

                            case "2":
                                print("\n--- REGISTRAR ENTRADA ---")

                                produto_id = int(
                                    input("ID do produto: ")
                                )

                                quantidade = int(
                                    input("Quantidade: ")
                                )

                                observacao = input(
                                    "Observação: "
                                )

                                registrar_entrada(
                                    produto_id,
                                    quantidade,
                                    observacao
                                )

                                print(
                                    "\nEntrada registrada com sucesso!"
                                )

                            case "3":
                                print("\n--- REGISTRAR SAÍDA ---")

                                produto_id = int(
                                    input("ID do produto: ")
                                )

                                quantidade = int(
                                    input("Quantidade: ")
                                )

                                observacao = input(
                                    "Observação: "
                                )

                                try:
                                    registrar_saida(
                                        produto_id,
                                        quantidade,
                                        observacao
                                    )

                                    print(
                                        "\nSaída registrada com sucesso!"
                                    )

                                except ValueError as erro:
                                    print(
                                        f"\nErro: {erro}"
                                    )

                            case "0":
                                break

                            case _:
                                print(
                                    "\nOpção inválida!"
                                )

                # =========================
                # RELATÓRIOS
                # =========================

                case "7":
                    while True:
                        print("\n--- RELATÓRIOS ---")
                        print("1 - Total de vendas")
                        print("2 - Produtos mais vendidos")
                        print("3 - Estoque baixo")
                        print("4 - Faturamento total")
                        print("0 - Voltar")

                        opcao_relatorio = input(
                            "Escolha uma opção: "
                        )

                        match opcao_relatorio:

                            case "1":
                                print("\n--- TOTAL DE VENDAS ---")

                                total_vendas = obter_total_vendas()

                                print(
                                    f"\nTotal de vendas: {total_vendas}"
                                )

                            case "2":
                                print(
                                    "\n--- PRODUTOS MAIS VENDIDOS ---"
                                )

                                produtos = (
                                    obter_produtos_mais_vendidos()
                                )

                                if produtos:
                                    for produto in produtos:
                                        print(
                                            f"Produto: {produto[0]} | "
                                            f"Quantidade vendida: "
                                            f"{produto[1]}"
                                        )
                                else:
                                    print(
                                        "\nNenhuma venda encontrada."
                                    )

                            case "3":
                                print("\n--- ESTOQUE BAIXO ---")

                                produtos = obter_estoque_baixo()

                                if produtos:
                                    for produto in produtos:
                                        print(
                                            f"ID: {produto[0]} | "
                                            f"Produto: {produto[1]} | "
                                            f"Estoque: {produto[2]} | "
                                            f"Mínimo: {produto[3]}"
                                        )
                                else:
                                    print(
                                        "\nNenhum produto com estoque baixo."
                                    )

                            case "4":
                                print(
                                    "\n--- FATURAMENTO TOTAL ---"
                                )

                                faturamento = (
                                    obter_faturamento_total()
                                )

                                print(
                                    f"\nFaturamento total: "
                                    f"R$ {faturamento:.2f}"
                                )

                            case "0":
                                break

                            case _:
                                print(
                                    "\nOpção inválida!"
                                )
                # =========================
                # SAIR
                # =========================

                case "0":
                    print("\nEncerrando o sistema...")
                    break

                case _:
                    print("\nOpção inválida!")

        except ValueError:
            print(
                "\nValor inválido. Digite um número onde for "
                "solicitado um ID, quantidade ou valor."
            )

        except Exception as erro:
            print(f"\nErro inesperado: {erro}")


if __name__ == "__main__":
    menu()