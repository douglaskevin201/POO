'''Inserindo um novo produto no banco de dados usando SQLAlchemy
    Inserindo um de cada vez.'''

novo_produto = Produto(
    nome='Notebook',
    preco=3500.00,
    estoque=10
)

session.add(novo_produto)
session.commit()
print(f"Produto criado com ID: {novo_produto.id}")

