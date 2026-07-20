tag_novo = Tag(nome='Novo')
tag_promocao = Tag(nome='promoção')
session.add.all([tag_novo, tag_promocao])
session.commit()

notebook = Produto(nome='Notebook')
notebook.tags.append(tag_novo)
notebook.tags.append(tag_promocao)
session.add(notebook)
session.commit()

print([tag.nome for tag in notebook.tags])
print([p.nome for p in tag_novo.produtos])
