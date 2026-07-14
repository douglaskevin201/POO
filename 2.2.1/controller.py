from model import Livro, LivroDAO
from view import menu, entrada_livro, listar_livros, mostrar_mensagem

class Controller:
    # Camada intermediária (padrão MVC) que conecta a View (entrada/saída do usuário)
    # com o Model/DAO (acesso ao banco de dados).
    def __init__(self, db_file):
        self.dao = LivroDAO(db_file)
        self.dao.conectar()      # abre a conexão com o banco assim que o Controller é criado
        self.dao.criar_tabela()  # garante que a tabela "livros" exista

    def inserir_livro(self):
        # Pede os dados do livro para a View, monta um objeto Livro (sem id, pois é novo)
        # e delega a inserção para o DAO.
        _, titulo, autor, ano, isbn = entrada_livro()  # o "_" descarta o id (não usado aqui)
        livro = Livro(id=None, titulo=titulo, autor=autor, ano=ano, isbn=isbn)
        if self.dao.inserir(livro):
            mostrar_mensagem("Livro inserido com sucesso.")
        else:
            mostrar_mensagem("Erro ao inserir livro.")

    def listar_livros(self):
        # Busca a lista de livros no DAO e repassa para a View exibir.
        livros = self.dao.listar()
        listar_livros(livros)

    def atualizar_livro(self):
        # Pede os dados (incluindo o id, por isso atualizar=True) e atualiza no banco.
        id, titulo, autor, ano, isbn = entrada_livro(atualizar=True)
        livro = Livro(id=id, titulo=titulo, autor=autor, ano=ano, isbn=isbn)
        if self.dao.atualizar(livro):
            mostrar_mensagem("Livro atualizado com sucesso.")
        else:
            mostrar_mensagem("Erro ao atualizar livro.")

    def deletar_livro(self):
        # Pede o id do livro a ser excluído.
        # try/except trata o caso do usuário digitar algo que não seja um número.
        try:
            livro_id = int(input("Digite o ID do livro para excluir: "))
            if self.dao.deletar(livro_id):
                mostrar_mensagem("Livro deletado com sucesso.")
            else:
                mostrar_mensagem("Livro não encontrado.")
        except ValueError:
            mostrar_mensagem("ID inválido.")