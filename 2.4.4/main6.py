'''exemplo de código escrito em Python que ensina como filtrar produtos
no banco de dados utilizando diferentes operadores de consulta em Python
com SQLAlchemy.'''


Produto.nome.ilike('%BOOK%')
Produto.preco.between(100, 500)
Produto.descricao.is_(None)
Produto.descricao.isnot(None)
Produto.nome.startswith('Note')
Produto.nome.endswith('Pro')
not_(Produto.preco > 1000)
