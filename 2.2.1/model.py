import sqlite3
from sqlite3 import Error

class Livro:
    def __init__(self, id, titulo, autor, ano, isbn):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.isbn = isbn

class LivroDAO:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None

    def conectar(self):
        try:
            self.conn = sqlite3.connect(self.db_file)
        except Error as e:
            print(f'Erro conectar banco: {e}')

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