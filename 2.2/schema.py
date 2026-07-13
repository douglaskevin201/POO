import sqlite3  # Módulo nativo do Python para SQLite

# Conectando (ou criando) o banco de dados
conexao = sqlite3.connect('meu_banco.db')  # Arquivo .db será criado se não existir
cursor = conexao.cursor()  # Cursor para executar comandos SQL

# Exemplo de DDL: Criando a tabela clientes
cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        email TEXT UNIQUE,
        telefone TEXT
    )
""")

# Exemplo de DML: Inserindo um registro
cursor.execute("""
    INSERT INTO clientes (nome, email, telefone)
    VALUES (?, ?, ?)
""", ('Maria Oliveira', 'maria@email.com', '11987654321'))

# Confirmando as mudanças (commit para DML)
conexao.commit()

# Exemplo de DML: Consultando dados
cursor.execute("SELECT * FROM clientes")
registros = cursor.fetchall()  # Busca todos os registros
for registro in registros:
    print(registro)  # Exibe: (1, 'Maria Oliveira', 'maria@email.com', '11987654321')

# Fechando a conexão (boa prática)
conexao.close()