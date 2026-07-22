'''exemplo de código escrito em Python que ensina como apagar
 um produto individual no banco de dados usando Python e a biblioteca SQLAlchemy.'''

# Exclui um produto específico buscando-o por id.

produto = session.query(Produto).filter_by(id=1).first()

if produto:
    session.delete(produto)
    session.commit()
    print("Produto deletado com sucesso")
else:
    print("Produto nao encontrado")
