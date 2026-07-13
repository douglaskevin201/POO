from controller import Controller
from view import menu, mostrar_mensagem

def main():
    controller = Controller('biblioteca.db')

    while True:
        opcao = menu()
        if opcao == '1':
            controller.inserir_livro()
        elif opcao == '2':
            controller.listar_livros()
        elif opcao == '3':
            controller.atualizar_livro()
        elif opcao == '4':
            controller.deletar_livro()
        elif opcao == '5':
            mostrar_mensagem('Saindo...')
            break
        else:
            mostrar_mensagem('Opção inválida')

if __name__ == '__main__':
    main()