from model import Livro, LivroDAO
from view import menu, entrada_livro, listar_livros, mostrar_mensagem

# Camada intermediária (padrão MVC) que conecta a View ao Model/DAO.
class Controller:
    def __init__(self, db_file):
        self.dao = LivroDAO(db_file)
        self.dao.conectar()
        self.dao.criar_tabela()

    # Pede os dados do livro para a View, monta um objeto Livro (sem id)
    # e delega a inserção para o DAO.
    def inserir_livro(self):
        _, titulo, autor, ano, isbn = entrada_livro()
        livro = Livro(id=None, titulo=titulo, autor=autor, ano=ano, isbn=isbn)
        if self.dao.inserir(livro):
            mostrar_mensagem("Livro inserido com sucesso.")
        else:
            mostrar_mensagem("Erro ao inserir livro.")

    # Busca a lista de livros no DAO e repassa para a View exibir.
    def listar_livros(self):
        livros = self.dao.listar()
        listar_livros(livros)

    # Pede os dados (incluindo o id) e atualiza no banco.
    def atualizar_livro(self):
        id, titulo, autor, ano, isbn = entrada_livro(atualizar=True)
        livro = Livro(id=id, titulo=titulo, autor=autor, ano=ano, isbn=isbn)
        if self.dao.atualizar(livro):
            mostrar_mensagem("Livro atualizado com sucesso.")
        else:
            mostrar_mensagem("Erro ao atualizar livro.")

    # Pede o id do livro a ser excluído e trata entrada inválida.
    def deletar_livro(self):
        try:
            livro_id = int(input("Digite o ID do livro para excluir: "))
            if self.dao.deletar(livro_id):
                mostrar_mensagem("Livro deletado com sucesso.")
            else:
                mostrar_mensagem("Livro não encontrado.")
        except ValueError:
            mostrar_mensagem("ID inválido.")