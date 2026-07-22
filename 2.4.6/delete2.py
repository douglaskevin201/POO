'''exemplo de código escrito em Python que ensina como excluir todos os produtos que estão sem 
estoque no banco de dados usando Python e a biblioteca SQLAlchemy, de acordo com o filtro aplicado.'''


# Exclui todos produtos sem estoque, de uma só vez.
linhas_excluidas = session.query(Produto).filter(
    Produto.estoque == 0
).delete()

session.commit()

print(f"{linhas_excluidas} produtos sem estoque foram removidos")
