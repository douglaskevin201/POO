def menu():
    print("\nMenu - Sistema Biblioteca")
    print("1 - Inserir livro")
    print("2 - Listar livros")
    print("3 - Atualizar livro")
    print("4 - Excluir livro")
    print("5 - Sair")
    return input("Escolha uma opção: ")

def entrada_livro(atualizar=False):
    if atualizar:
        id = int(input("Digite o ID do livro: "))
    else:
        id = None
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = int(input("Ano: "))
    isbn = input("ISBN: ")
    return id, titulo, autor, ano, isbn

def listar_livros(livros):
    print("\nLista de Livros:")
    if not livros:
        print("Nenhum livro encontrado.")
        return
    for livro in livros:
        print(f"ID: {livro.id}, Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano}, ISBN: {livro.isbn}")

def mostrar_mensagem(msg):
    print(msg)