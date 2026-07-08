# Modificando o exemplo anterior.
# Inserindo o método desenhar a classe quadrado previamente definida
# Neste Exemplo, estamos aumentando a responsabilidade da classe quadrado inserindo mais um metodo


from abc import ABC, abstractmethod

class FormaGeometrica(ABC):

    @abstractmethod
    def calcular_area(self):
        pass

class Quadrado(FormaGeometrica):
    def __init__(self, base):
        self.base = base

    def calcular_area(self):
        figura = ['quadrado']
        figura.append(self.base * self.base)
        return figura
    
    def desenhar(self):
        # desenha um quadrado
        print("Desenha um quadrado!")
        pass

    
