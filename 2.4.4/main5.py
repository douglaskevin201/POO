''''Exemplo prático de como criar consultas mais avançadas em bancos de dados'''


from sqlalchemy import and_, or_, not_

produtos = session.query(Produto).filter(
    and_(Produto.preco > 100, Produto.estoque > 0)
).all()

produtos = session.query(Produto).filter(
    or_(Produto.preco < 50, Produto.preco > 1000)
).all()

produtos = session.query(Produto).filter(
    Produto.nome.like('%book%')
).all()

produtos = session.query(Produto).filter(
    Produto.id.in_([1, 3, 5])
).all()

