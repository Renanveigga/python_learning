produto = {"pc": 2000}

def exibir_produtos():
         if not produto:
              print("Nenhum item cadastrado")
              return

         for nome, preco in produto.items():
            print("produtos cadastrados!")
            print(f"{len(produto)} produtos cadastrados")
            print(f"produto: {nome}, preço: R${preco:.2f}")
            print()

def sair():
    print("Saindo do programa...")
    exit() # função exit() encerra o programa

def menu_cadastro_produto():
    print("===== MENU DE CADASTRO DE PRODUTOS =====")
    print("1. Cadastrar Produto")
    print("2. Listar Produtos")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("===== CADASTRO DE PRODUTOS =====")
        nome_produto = input("Digite o nome do produto: ")
        preco_produto = float(input("Digite o preço do produto: "))
        produto[nome_produto] = preco_produto # Adiciona o produto ao dicionário com o nome como chave e o preço como valor

    elif opcao == "2":
        exibir_produtos()   

    elif opcao == "3":
        sair()
 
while True:
    menu_cadastro_produto()