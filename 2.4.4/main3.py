'''
Linha 9: consulta todos os produtos, ordenando por preço decrescente.

Linha 11: consulta os primeiros 5 produtos da tabela.

Linha 13: pega 10 produtos após ignorar os 10 primeiros
'''

produtos_ordenados = session.query(Produto).order_by(Produto.preco.desc()).all()

primeiros_5 = session.query(Produto).limit(5).all()

produtos_pagina_2 = session.query(Produto).offset(10).limit(10).all


