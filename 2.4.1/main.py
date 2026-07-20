
eletronicos = Categoria(nome='Eletronicos')
notebook = Produto(nome='Notebook', categoria=eletronicos)
mouse = Produto(nome='Mouse', categoria_id=1)

for produto in eletronicos.produtos:
    print(produto.nome)

print(notebook.categoria.nome)
