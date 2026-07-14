def menu():
    # Responsável apenas por exibir as opções e capturar a escolha do usuário.
    # Não tem nenhuma lógica de negócio (isso é papel do Controller).
    print("\nMenu - Sistema Biblioteca")
    print("1 - Inserir livro")
    print("2 - Listar livros")
    print("3 - Atualizar livro")
    print("4 - Excluir livro")
    print("5 - Sair")
    return input("Escolha uma opção: ")

def entrada_livro(atualizar=False):
    # Coleta os dados de um livro digitados pelo usuário.
    # Se for atualização, também pede o ID (para saber qual livro alterar).
    if atualizar:
        id = int(input("Digite o ID do livro: "))
    else:
        id = None  # inserção não precisa de ID, o banco gera automaticamente
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = int(input("Ano: "))
    isbn = input("ISBN: ")
    return id, titulo, autor, ano, isbn  # retorna tupla com todos os dados

def listar_livros(livros):
    # Exibe na tela a lista de livros recebida do Controller.
    print("\nLista de Livros:")
    if not livros:
        print("Nenhum livro encontrado.")
        return
    for livro in livros:
        print(f"ID: {livro.id}, Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano}, ISBN: {livro.isbn}")

def mostrar_mensagem(msg):
    # Função genérica para exibir mensagens de feedback ao usuário
    # (sucesso, erro, avisos, etc).
    print(msg)