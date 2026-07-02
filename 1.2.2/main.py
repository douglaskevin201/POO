#importando a classe Cachorro
from cachorro import Cachorro

#criação de um objeto (instancia) da classe cachorro

meu_cachorro = Cachorro(apelido="Rex", idade=5, raca="Labrador")
#saida - criando um novo cachorro chamado Rex...


#acessando os atributos do objeto 
print("\n--- Atributos do Cachorro ---") 
print(f"Apelido: {meu_cachorro.apelido}")#saida: apelido: Rex
print(f"idade: {meu_cachorro.idade}")#saida: idade: 5
print(f"raca: {meu_cachorro.raca}")#saida: raca: Labrador


#chamando os metodos do objeto
print("\n--- Acoes (Metodos) do cachorro ---")
meu_cachorro.sentar()#saida: Rex sentou!
meu_cachorro.rolar()#saida: Rex rolou!
meu_cachorro.correr(velocidade="lentamente")#saida: Rex está correndo lentamente
meu_cachorro.comer("racao")#saida: Rex está comendo ração

print("\n-----------------------------------")

#criando outro cachorro da mesma classe para demonstrar a reutilização
outro_cachorro = Cachorro(apelido="Luna", idade=2, raca="Golden Retriever")
print(f"\nConheca a {outro_cachorro.apelido}, uma {outro_cachorro.raca} de {outro_cachorro.idade} anos.")
outro_cachorro.sentar() #saida: Luna Sentou!
