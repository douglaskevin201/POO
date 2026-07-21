'''Criando varios produtos de uma vez e inserindo no banco com session.add_all(...)
    Criado a partir de uma lista comum do python.'''

produtos = [
    Produto(nome='Mouse', preco=50.00, estoque=100),
    Produto(nome='Teclado', preco=150.00, estoque=50),
    Produto(nome='Monitor', preco=800.00, estoque=25)
]

session.add_all(produtos)
session.commmit()

for produto in produtos:
    print(f"{produto.nome}: ID = {produto.id}")
