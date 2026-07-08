class Animal:
    '''Classe base para todos os animais'''
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        return "Som genérico de Animal"
    
    def informacoes(self):
        return f"{self.nome}, {self.idade} anos"
    

class Cachorro(Animal):
    """Cachorro herda de Animal"""
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)#chama __init__ de Animal 
        self.raca = raca

    def emitir_som(self):
        return "Au au!"
    
    def abanar_rabo(self):
        return f"{self.nome} esta abanando o rabo"
    

class Gato(Animal):
    """Gato herda de Animal"""
    def __init__(self, nome, idade, cor_pelo):
        super().__init__(nome, idade)
        self.cor_pelo = cor_pelo

    def emitir_som(self):
        return "Miau!"
    
    def arranhar(self):
        return f"{self.nome} esta arranhando"
    
rex = Cachorro("Rex", 5, "Labrador")
mimi = Gato("Nala", 3, "Branca")

print(f"{rex.informacoes()}") #herdado de Animal. 
print(f"{rex.emitir_som()}") #sobrescrito em Cachorro
print(f"{rex.abanar_rabo()}") #especifico de Cachorro

print(f"{mimi.informacoes()}") #herdado de Animal
print(f"{mimi.emitir_som()}") #sobrescrito em Gato
print(f"{mimi.arranhar()}") #especifico de Gato


    