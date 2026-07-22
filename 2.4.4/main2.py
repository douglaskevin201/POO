produto =  session.query(Produto).filter_by(id=1).first()
produtos_caros = session.query(Produto).filter(Produto.preco > 1000).all()
produtos_filtrados = session.query(Produto).filter(
    Produto.preco > 100,
    Produto.estoque > 0,
).all()

session.query(Produto).filter_by(nome='mouse', preco=50.00)
session.query(Produto).filter(Produto.nome == 'Mouse', Produto.preco > 50)

