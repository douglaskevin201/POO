'''Buscando todos os registros - CRUD - READ'''

todos_produtos = session.query(Produto).all()

for produto in todos_produtos:
    print(Produto)
