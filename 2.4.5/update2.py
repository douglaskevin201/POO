'''Atualização em lote para reabastecer produtos com estoque baixo.'''

# Filtra produtos com estoque menor que 10. Seleciona todos os produtos
# com estoque abaixo de 10 e da um update 'estoque': 20
# todos os registros selecionados serão afetados
linhas_afetadas = session.query(Produto).filter(
    Produto.estoque < 10
).update({
    'estoque': 20
})

session.commit() # Confirma no banco de dados

# Exibe resultado indicando quantas linhas de produtos foram afetadas
# e quantos produtos tiveram o estoque alterado 
print(f"{linhas_afetadas} produtos reabastecidos")

