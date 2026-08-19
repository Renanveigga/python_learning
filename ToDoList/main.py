# Lista de coisas a se fazerem
tarefas = {
    "ir ao mercado": {"descricao": "fazer compras", "concluida": False}
}

def adicionar_tarefa():
    print("=====ADICIONAR TAREFA=====")
    nome_task = input("\nAdicione um nome para a tarefa: ").lower().strip()
    task = input("Adicione uma descrição: ").lower().strip()

    tarefas[nome_task] = {
        "descricao": task,
        "concluida": False
    }
    print(f"'{nome_task}' adicionado com sucesso!\n")

def marcar_concluido():
    print("=====Marcar Tarefa concluída=====")
    print("\nTarefas pendentes:")

    # Exibe apenas as tarefas não concluídas
    for nome, dados in tarefas.items():
        if not dados["concluida"]:
            print(f"- {nome}: {dados['descricao']}")

    decisao = input("\nDeseja marcar alguma tarefa como concluída? [s/n]: ").lower().strip()   

    if decisao == "s":
        qual_tarefa = input("Qual o nome da tarefa a ser concluída? ").lower().strip()
        
        if qual_tarefa in tarefas:
            tarefas[qual_tarefa]["concluida"] = True
            print("Tarefa concluída com sucesso!\n")
        else:
            print("Tarefa não encontrada!\n")
    else:
        print("Nenhuma alteração feita.\n")

def exibir_tarefa():
    print("\n=====Tarefas=====")
    print(f"Total: {len(tarefas)} tarefas cadastradas")
    
    for task, dados in tarefas.items():
        status = "Concluída" if dados["concluida"] else "Pendente"
        print(f"• Tarefa: {task} | Status: {status}")
        print(f"  Descrição: {dados['descricao']}\n")

def excluir_tarefa():
    if not tarefas:
            print("\nNenhuma tarefa cadastrada para remover.")
            return

    excluir = input("Deseja excluir alguma tarefa? [s/n]").lower().strip()        
    if excluir == "s":
        for task, dados in tarefas.items():
          print(f"• Tarefa: {task} ")
          print(f"  Descrição: {dados['descricao']}\n")
        qual_tarefa = input("Qual tarefa deseja excluir?")

        del(tarefas[qual_tarefa])
        if qual_tarefa not in tarefas:
                          print("Produto não encontrado!")
    else:
        print(f"\n cancelando exclusão")    

 
def sair():
    print("Encerrando aplicação...")
    exit()

def menu_tarefa():
    print("=====MENU TO DO LIST=====")
    print("1. Adicionar Tarefa")
    print("2. Marcar Tarefa Concluída")
    print("3. Exibir Tarefas")
    print("4. Excluir Tarefa")
    print("5. Sair")
    
    try:
        opcao = int(input("Escolha uma opção: "))
        print()

        if opcao == 1:
            adicionar_tarefa()
        elif opcao == 2:
            marcar_concluido()
        elif opcao == 3:
            exibir_tarefa()

        elif opcao == 4:
            excluir_tarefa()
         
        elif opcao == 5:
            sair()
        else:
            print("Opção inválida!\n")
    except ValueError:
        print("Por favor, digite apenas números.\n")

while True:
    menu_tarefa()