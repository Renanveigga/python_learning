produto = {"pc": 2000}

def exibir_produtos():
         if not produto:
              print("Nenhum item cadastrado")
              return
         
         print("\nprodutos cadastrados!")
         for nome, preco in produto.items():
            print(f"{len(produto)} produtos cadastrados")
            print(f"produto: {nome}, preço: R${preco:.2f}\n")

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

        while True:
            try:
                preco_produto = float(input("Digite o preço do produto: "))
                
                # Verificação de preço negativo
                if preco_produto < 0:
                    print("Erro: O preço do produto não pode ser negativo! Tente novamente.\n")
                    continue  # Ignora o resto do laço e volta para o início do 'while'
                
                break  # Se o número for válido e maior ou igual a zero, quebra o laço 'while'

            except ValueError:
                print("\nDigite uma opção válida de preço (use ponto para decimais).")

        
    elif opcao == "2":
        exibir_produtos()   

    elif opcao == "3":
        sair()

    else:
         print("\nOpçao inválida")
         print("Digite uma opção válida para prosseguir\n")    
 
while True:
    menu_cadastro_produto()