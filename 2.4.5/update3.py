'''Atualização em lote, aumentando em 10%
 o preço de todos os produtos acima de 1000.'''


session.query(Produto).filter( # Filtra produtos
    Produto.preco > 1000 # seleciona todos os produtos com valor acima de 1000
).update({ # Inicia Atualização
    # atualiza com expessão matematica
    'preco': Produto.preco * 1.1 # para cada produto selecionado, o preço é
    # multiplicado por 1.1(aumenta 10%)
}, synchronize_session='fetch')# garante que a sessão Python do SQLAlchemy será atualizada com o novo valor.

session.commit()
