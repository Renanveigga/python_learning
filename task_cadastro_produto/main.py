produto = {"pc": 2000}
categoria_produto = ["informática", "cosmético", "utilidade","outro"]  # adicionar categoria e qtd. estoque

def exibir_produtos():
         if not produto:
              print("Nenhum item cadastrado")
              return
         
         print("\n====produtos cadastrados=====")
         print(f"{len(produto)} produtos cadastrados")
         for nome, preco, categoria_produto in produto.items():
            print(f"produto: {nome}, preço: R${preco:.2f} e categoria {categoria_produto}\n")

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
 
        busca = input("Digite um produto a ser buscado: ").strip()

        if busca in produto:
            preco = produto[busca]
            print("\nProduto encontrado!")
            print(f"Nome: {busca}")
            print(f"Preço: R${preco:.2f}\n")
             
        else:
            print("\nProduto não encontrado!\n")    
           
def estatisticas():

    if not produto: 
        print("\nNenhum produto cadastrado para gerar estatísticas.")
        return

    total = len(produto) #total de produtos dentro do dicionário
    maior_preco = max(produto, key=produto.get) #verifica maior valor dentro do dicionário
    preco_maior = produto[maior_preco]

    menor_preco = min(produto, key=produto.get) #verifica menor dentro do dicionário
    preco_menor = produto[menor_preco]

    media_preco = sum(produto.values()) / total # Soma todos os valores e divide pelo total de itens

    print("\n===== ESTATÍSTICAS =====")
    print(f"Total de produtos: {total}")
    print(f"\nProduto mais caro:")
    print(f"{maior_preco} - R${preco_maior:.2f}\n")
    print(f" Produto mais barato:")
    print(f"{menor_preco} - R${preco_menor:.2f}\n")
    print(f"Preço médio: ")
    print(f"R${media_preco:.2f}")

def sair():
    print("Saindo do programa...")
    exit() # função exit() encerra o programa

def menu_cadastro_produto():
    print("===== MENU DE CADASTRO DE PRODUTOS =====")
    print("1. Cadastrar Produto")
    print("2. Listar Produtos")
    print("3. Buscar Produto")
    print("4. Excluir Produto")
    print("5. Estatísticas")
    print("6. Produtos com estoque baixo")
    print("7. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("===== CADASTRO DE PRODUTOS =====")

        while True:
            nome_produto = input("Digite o nome do produto: ").lower().strip()
            
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

        while True:
          try:
           print ("Escolha a categoria do produto entre essas opções") 
           print (f"{categoria_produto}")   
           escolha_categ = input("Qual categoria deseja escolher: ").lower().strip
           if escolha_categ not in categoria_produto:
            print("Escolha uma categoria válida")
            continue

           break
          except ValueError:
              print("Não é uma categoria pré-determinada, escolha outra") 


        produto[nome_produto] = preco_produto
        produto[categoria_produto] = escolha_categ
        print(f"Produto '{nome_produto}' cadastrado com sucesso!\n")        
        
    elif opcao == "2":
        exibir_produtos()   

    elif opcao == "3":
        buscar_produto()    

    elif opcao == "4":
        remover_produto()    

    elif opcao == "5":
        estatisticas()

    elif opcao == "7":
        sair()    

    else:
         print("\nOpçao inválida")
         print("Digite uma opção válida para prosseguir\n")    
 
while True:
    menu_cadastro_produto()