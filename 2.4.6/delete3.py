session.query(Produto).delete() # PERIGOSO!!
session.query(Produto).filter(Produto.id == 1).delete() # SEGURO!!


'''Mostra os riscos da exclusão sem filtro.
Implementa confirmação antes de remover em lote,
tornando o código mais seguro para produção.'''

produtos_sem_estoque = session.query(Produto).filter(
    Produto.estoque == 0
).all()

if produtos_sem_estoque:
    resposta = input(f"Excluir {len(produtos_sem_estoque)} produtos? (s/n): ")
    if resposta.lower() == 's':
        session.query(Produto).filter(Produto.estoque == 0).delete()
        session.commit()
        print("Produtos excluidos!")

