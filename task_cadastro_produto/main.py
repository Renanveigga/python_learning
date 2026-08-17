produto = {"pc": 2000}

def exibir_produtos():
         if not produto:
              print("Nenhum item cadastrado")
              return
         
         print("\n====produtos cadastrados=====")
         print(f"{len(produto)} produtos cadastrados")
         for nome, preco in produto.items():
            print(f"produto: {nome}, preço: R${preco:.2f}\n")

def remover_produto(): 

    if not produto:
        print("\nNenhum produto cadastrado para remover.")
        return # Para a função se não houver produto a ser removido
    
    while True:
      item_escolhido = input("Digite o produto que deseja excluir: ").strip()

      if item_escolhido not in produto:
          print("Produto não encontrado!")

          continue
      break

    confirmacao = input(f"Deseja mesmo excluir {item_escolhido} [s/n]: ").lower().strip()

    if confirmacao == 's':
      del(produto[item_escolhido])   
      print(f"Produto {item_escolhido} excluído com sucesso!\n")  
    else:
        print("Cancelando exclusão\n") 

def buscar_produto():
    while True:
     try:
        busca = input("Digite um produto a ser buscado: ")

        if busca in produto:
            print("\nProduto encontrado!")
            print(f"Nome: {busca}")
            print(f"Preço: {produto[busca]}\n")
            break
        else:
            print("\nProduto não encontrado!\n")

     except ValueError:
        print(f"Erro ao buscar produto: {busca}")



def sair():
    print("Saindo do programa...")
    exit() # função exit() encerra o programa

def menu_cadastro_produto():
    print("===== MENU DE CADASTRO DE PRODUTOS =====")
    print("1. Cadastrar Produto")
    print("2. Listar Produtos")
    print("3. Buscar Produto")
    print("4. Excluir Produto")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("===== CADASTRO DE PRODUTOS =====")

        while True:
            nome_produto = input("Digite o nome do produto: ").strip()
            
            if not nome_produto:
                print("Digite um nome válido")
            elif nome_produto in produto:
                print(f"Produto {nome_produto} já cadastrado ⚠")   
                continue
            break

        while True:
            try:
                preco_produto = float(input("Digite o preço do produto: "))
                
                # Verificação de preço negativo
                if preco_produto < 0:
                    print("Erro: O preço do produto não pode ser negativo! Tente novamente.\n")
                    continue  # Ignora o resto do laço e volta para o início do 'while'
                
                break  # Se o número for válido e maior ou igual a zero, quebra o laço 'while'

            except ValueError:
                print("\nDigite uma opção válida de preço.")

        produto[nome_produto] = preco_produto
        print(f"Produto '{nome_produto}' cadastrado com sucesso!\n")        
        
    elif opcao == "2":
        exibir_produtos()   

    elif opcao == "3":
        buscar_produto()    

    elif opcao == "4":
        remover_produto()    

    elif opcao == "5":
        sair()

    else:
         print("\nOpçao inválida")
         print("Digite uma opção válida para prosseguir\n")    
 
while True:
    menu_cadastro_produto()