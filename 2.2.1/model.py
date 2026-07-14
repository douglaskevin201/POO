import sqlite3
from sqlite3 import Error

class Livro:
    # Classe "entidade" (Model) que representa um Livro.
    # Serve apenas para guardar os dados, sem lógica de banco.
    def __init__(self, id, titulo, autor, ano, isbn):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.isbn = isbn

class LivroDAO:
    # DAO = Data Access Object.
    # Classe responsável por toda a comunicação com o banco SQLite,
    # isolando o SQL do resto da aplicação (Controller/View).
    def __init__(self, db_file):
        self.db_file = db_file  # caminho/nome do arquivo .db
        self.conn = None        # conexão será criada em conectar()

    def conectar(self):
        # Abre a conexão com o banco de dados SQLite.
        # sqlite3.connect cria o arquivo .db automaticamente se não existir.
        try:
            self.conn = sqlite3.connect(self.db_file)
        except Error as e:
            print(f'Erro conectar banco: {e}')

    def criar_tabela(self):
        # Cria a tabela "livros" caso ela ainda não exista.
        # IF NOT EXISTS evita erro se o programa rodar mais de uma vez.
        try:
            sql = (
            "CREATE TABLE IF NOT EXISTS livros ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, "  # chave primária auto-incrementada
            "titulo TEXT NOT NULL, "                   # título é obrigatório
            "autor TEXT NOT NULL, "                    # autor é obrigatório
            "ano INTEGER, "                             # ano é opcional (pode ser NULL)
            "isbn TEXT"                                 # isbn é opcional
            ");"
            )
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()  # confirma a criação da tabela no banco
        except Error as e:
            print(f'Erro criar tabela: {e}')

    def inserir(self, livro):
        # Insere um novo livro na tabela.
        # Usa "?" (query parametrizada) para evitar SQL Injection.
        try:
            sql = 'INSERT INTO livros (titulo, autor, ano, isbn) VALUES (?, ?, ?, ?)'
            cursor = self.conn.cursor()
            cursor.execute(sql, (livro.titulo, livro.autor, livro.ano, livro.isbn))
            self.conn.commit()
            return cursor.lastrowid  # retorna o ID gerado automaticamente pelo SQLite
        except Error as e:
            print(f'Erro inserir livro: {e}')
            return None

    def listar(self):
        # Busca todos os livros cadastrados no banco.
        try:
            sql = 'SELECT * FROM livros'
            cursor = self.conn.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()  # lista de tuplas (id, titulo, autor, ano, isbn)
            # Converte cada tupla retornada do banco em um objeto Livro
            livros = [Livro(id=row[0], titulo=row[1], autor=row[2], ano=row[3], isbn=row[4]) for row in rows]
            return livros
        except Error as e:
            print(f'Erro listar livros: {e}')
            return []

    def atualizar(self, livro):
        # Atualiza os dados de um livro já existente, identificado pelo id.
        try:
            sql = 'UPDATE livros SET titulo=?, autor=?, ano=?, isbn=? WHERE id=?'
            cursor = self.conn.cursor()
            cursor.execute(sql, (livro.titulo, livro.autor, livro.ano, livro.isbn, livro.id))
            self.conn.commit()
            return cursor.rowcount  # quantidade de linhas afetadas (0 = id não encontrado)
        except Error as e:
            print(f'Erro atualizar livro: {e}')
            return 0

    def deletar(self, livro_id):
        # Remove um livro do banco a partir do seu id.
        try:
            sql = 'DELETE FROM livros WHERE id=?'
            cursor = self.conn.cursor()
            cursor.execute(sql, (livro_id,))
            self.conn.commit()
            return cursor.rowcount  # 0 = nenhum livro com esse id foi encontrado
        except Error as e:
            print(f'Erro deletar livro: {e}')
            return 0