from task_manager import TaskManager

def menu():
    print("\n🗓️ GERENCIADOR DE TAREFAS 🗓️")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Marcar tarefa como concluída")
    print("4 - Sair")

def main():
    manager = TaskManager()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome da tarefa: ")
            manager.adicionar_tarefa(nome)

        elif opcao == "2":
            manager.listar_tarefas()

        elif opcao == "3":
            manager.listar_tarefas()
            indice = int(input("Digite o número da tarefa para concluir: "))
            manager.marcar_concluida(indice)

        elif opcao == "4":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
