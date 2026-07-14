import sqlite3
from sqlite3 import Error

# Classe "entidade" (Model) que representa um Livro.
# Serve apenas para guardar os dados, sem lógica de banco.
class Livro:
    def __init__(self, id, titulo, autor, ano, isbn):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.isbn = isbn

# DAO = Data Access Object.
# Classe responsável por toda a comunicação com o banco SQLite,
# isolando o SQL do resto da aplicação (Controller/View).
class LivroDAO:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None

    # Abre a conexão com o banco de dados SQLite.
    # sqlite3.connect cria o arquivo .db automaticamente se não existir.
    def conectar(self):
        try:
            self.conn = sqlite3.connect(self.db_file)
        except Error as e:
            print(f'Erro conectar banco: {e}')

    # Cria a tabela "livros" caso ela ainda não exista.
    # IF NOT EXISTS evita erro se o programa rodar mais de uma vez.
    def criar_tabela(self):
        try:
            sql = (
            "CREATE TABLE IF NOT EXISTS livros ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "titulo TEXT NOT NULL, "
            "autor TEXT NOT NULL, "
            "ano INTEGER, "
            "isbn TEXT"
            ");"
            )
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
        except Error as e:
            print(f'Erro criar tabela: {e}')

    # Insere um novo livro na tabela.
    # Usa "?" (query parametrizada) para evitar SQL Injection.
    def inserir(self, livro):
        try:
            sql = 'INSERT INTO livros (titulo, autor, ano, isbn) VALUES (?, ?, ?, ?)'
            cursor = self.conn.cursor()
            cursor.execute(sql, (livro.titulo, livro.autor, livro.ano, livro.isbn))
            self.conn.commit()
            return cursor.lastrowid
        except Error as e:
            print(f'Erro inserir livro: {e}')
            return None

    # Busca todos os livros cadastrados no banco.
    def listar(self):
        try:
            sql = 'SELECT * FROM livros'
            cursor = self.conn.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            livros = [Livro(id=row[0], titulo=row[1], autor=row[2], ano=row[3], isbn=row[4]) for row in rows]
            return livros
        except Error as e:
            print(f'Erro listar livros: {e}')
            return []

    # Atualiza os dados de um livro já existente, identificado pelo id.
    def atualizar(self, livro):
        try:
            sql = 'UPDATE livros SET titulo=?, autor=?, ano=?, isbn=? WHERE id=?'
            cursor = self.conn.cursor()
            cursor.execute(sql, (livro.titulo, livro.autor, livro.ano, livro.isbn, livro.id))
            self.conn.commit()
            return cursor.rowcount
        except Error as e:
            print(f'Erro atualizar livro: {e}')
            return 0

    # Remove um livro do banco a partir do seu id.
    def deletar(self, livro_id):
        try:
            sql = 'DELETE FROM livros WHERE id=?'
            cursor = self.conn.cursor()
            cursor.execute(sql, (livro_id,))
            self.conn.commit()
            return cursor.rowcount
        except Error as e:
            print(f'Erro deletar livro: {e}')
            return 0