# Lista de coisas a se fazerem
tarefas = {
"ir ao mercado": {"description": "fazer compras", "concluida": False,  }
}


def adicionar_tarefa():
    print("=====ADICIONAR TAREFA=====")
    nome_task = input("\nAdicione um nome para a tarefa: ").lower().strip()
    task = input("\nAdicione uma tarefa: ").lower().strip()

    

    tarefas[nome_task] = {
        "descricao": task,
        "concluida": False
    }
    print(f"{nome_task} adicionado com sucesso!\n")

def marcar_concluido():
   print("=====Marcar Tarefa concluída=====")
   print(f"\nTarefas a serem concluídas")

   for nome, dados in tarefas.items():
      print(f"{nome}: {dados}")

   decisao = input(f"Deseja marcar alguma tarefa como concluída? [s/n]").lower().strip()   

   if decisao == "s":
      tarefas['concluida'] = True
      print("Tarefa concluída com sucesso!") 
   else:
      print("A tarefa não foi concluída")    

def exibir_tarefa():
   print("\n=====Tarefas a serem feitas=====")
   print(f"\n{len(tarefas)} tarefas para serem feitas")
   for task, description in tarefas.items():
      print(f"tarefa '{task}' a ser feita, que diz a respeito de: \n{description}\n")

def sair():
    print("Encerrando aplicação")
    exit()

def menu_tarefa():
    print("=====MENU TO DO LIST=====")
    print("1.Adicionar Tarefa")
    print("2.Marcar Tarefa Concluída")
    print("3.Exibir Tarefa")
    print("4.Excluir Tarefa")
    print("5.Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
     adicionar_tarefa()

    elif opcao == 2:
       marcar_concluido()

    elif opcao == 3:
       exibir_tarefa()

    elif opcao == 5:
       sair()

while True:
    menu_tarefa()    