produtos = session.query(Produto).filter(
    or_(
        and_(Produto.preco < 100, Produto.estoque > 0),
        and_(Produto.preco > 1000, Produto.estoque < 5)
    )
).all()
