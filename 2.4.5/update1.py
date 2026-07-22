# Busca o produto por id. Retorna o primeiro com id=1
produto = session.query(Produto).filter_by(id=1).first()


if produto: # Se produto existe...
    # Altera os campos de produto
    produto.preco = 3800.00
    produto.estoque = 8
    
    session.commit()# Confirma no banco salvando as atualizações no banco de dados

    # Exibe mensagem se o produto foi encontrado e alterado
    print(f"Produto {produto.nome} atualizado com sucesso!")
    
else:# Se não foi encontrado, informa o usuario.    
    print("Produto nao encontrado!")
