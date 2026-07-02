class Cachorro:
    
    def __init__(self, apelido, idade, raca):
        #inicializa um novo objeto Cachorro
        print(f"Criando um novo cachorro chamado {apelido}...")
        self.apelido = apelido
        self.idade = idade
        self.raca = raca

    def sentar(self):
        #simula cachorro sentando
        print(f"{self.apelido} sentou!")


    def rolar(self):
        #simula cachorro rolando
        print(f"{self.apelido} rolou no chao!")


    def correr(self, velocidade="rapidamente"):
        #simula cachorro correndo
        print(f"{self.apelido} esta correndo {velocidade}!")


    def comer(self, comida):
        #simula cachorro comendo algo
        print(f"{self.apelido} esta comendo {comida}!")
    

    
    