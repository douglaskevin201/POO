# Importando o módulo nativo do python para SQLite
import sqlite3

# Passo1: conectando (ou criando) o banco de dados 
# Arquivo meu_banco.db será criado se não existir 
conexao = sqlite3.connect('meu_banco.db')

# Passo2: Criando o crusor para manipular os dados do banco de dados 
# Cursor para exutar comandos SQL
cursor = conexao.cursor()

# Passo3: Executando comandos SQL 
# Exemplo de DDL: Criando a tabela clientes 
cursor.execute("""
    CREATE TABLE IF NOT EXIST clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        nome TEXT NOT NULL, 
        email TEX UNIQUE, 
        telefone TEXT
    )
""")

# Passo3: Executando comandos SQL(continuação)
# Exemplo de DML: Inserindo um registro
cursor.execute("""
    INSERT INTO clientes (nome, email, telefone)
    VALUES ('Maria Oliveira', 'maria@email.com', '11999999999')
""")

# Passo4: Efetuando o commit para salvar as alterções
# Confirmando as mudanças (commit para DML)
conexao.commit()

# Passo3 Executando comandos SQL (continuação)
# Exemplo de DML: Consultando dados
cursor.execute("SELECT * FROM clientes")
# Busca todos os registros
registros = cursor.fetchall()
for registro in registros:
    # Exibe: (1, 'Maria Oliveira', 'maria@email.com', '11999999999')
    print(registro)

# Passo5: fechar a conexão com o banco de dados após o uso
# Fechando a conexão(boa pratica)
conexao.close()


