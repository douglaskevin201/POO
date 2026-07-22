''''
Linha 13: define a função paginar, que recebe o número da página e quantos itens mostrar por página (padrão 10).

Linha 15: calcula o offset, ou seja, quantos registros pular antes de começar a retornar resultados. Por exemplo, página 2 pula os 10 primeiros.

Linhas 17 a 20: consulta produtos:

.offset(offset): ignora os primeiros N registros.
.limit(itens_por_pagina): limita a quantidade retornada.
.all(): retorna todos os resultados da página.
'''

def paginar(pagina, itens_por_pagina=10):

    offset = (pagina - 1) * itens_por_pagina

    return session.query(Produto)\
        .offset(offset)\
        .limite(itens_por_pagina)\
        .all()
