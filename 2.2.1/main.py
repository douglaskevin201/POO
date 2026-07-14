from controller import Controller
from view import menu, mostrar_mensagem

# Ponto de entrada do programa.
def main():
    controller = Controller('biblioteca.db')

    # Loop principal: mantém o menu rodando até o usuário escolher "Sair".
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

# Só executa main() se o arquivo for rodado diretamente.
if __name__ == '__main__':
    main()