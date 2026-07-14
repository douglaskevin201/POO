from controller import Controller
from view import menu, mostrar_mensagem

def main():
    # Ponto de entrada do programa.
    # Cria o Controller, que por sua vez conecta ao banco e garante a tabela.
    controller = Controller('biblioteca.db')

    # Loop principal: mantém o menu rodando até o usuário escolher "Sair".
    while True:
        opcao = menu()  # exibe o menu e captura a opção digitada
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
            break  # encerra o while True e finaliza o programa
        else:
            mostrar_mensagem('Opção inválida')

# Garante que main() só rode quando este arquivo for executado diretamente
# (e não quando for importado por outro módulo).
if __name__ == '__main__':
    main()