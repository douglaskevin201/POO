

# Exemplo de implementação de classes concretas
# Foram criados dois metodos para a classe que representa uma Figura Geometrica 
# O método __init__ responsavel por construir os objetos da classe 
# O método calcular_area responsável por efetuar o cálculo da area conforme a Figura Géometrica, porém, utiliza 
# O mesmo método definido na classe abstrata com devidas particularidades 
# O calculo da área será refeito para cada figura, segundo seu comportamento

import math
from abc import ABC, abstractmethod

class FormaGeometrica(ABC):

    @abstractmethod
    def calcular_area(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        figura = ['Retangulo']
        figura.append(self.base * self.altura)
        return figura
    

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        figura = ['Circulo']
        figura.append(self.raio * self.raio * math.pi)
        return figura
    
    

class Quadrado(FormaGeometrica):
    def __init__(self, base):
        self.base = base
    
    def calcular_area(self):
        figura = ['Quadrado']
        figura.append(self.base * self.base)
        return figura
    
# Exemplo do uso de polimorfismo 
# A variavel retangulo1 representa um retangulo de base 4cm e altura 8cm
# A variavel retangulo2 representa um retangulo de base 6cm e algura 10cm
# A variavel quadrado1 representa um quadrado com 4cm de lado 
# A variavel quadrado2 representa um quadrado com 6cm de lado 
# A variavel circulo1 representa um circulo de 4cm de raio
# A variavel circulo2 representa um circulo de 6cm de raio 
# A variavel formas_geometricas armazena uma lista de figuras

retangulo1 = Retangulo(4, 8)
retangulo2 = Retangulo(6, 10)
quadrado1 = Quadrado(4)
quadrado2 = Quadrado(6)
circulo1 = Circulo(4)
circulo2 = Circulo(6)

formas_geometricas = [retangulo1, retangulo2, quadrado1, quadrado2, circulo1, circulo2]

area = 0
for i, forma in enumerate(formas_geometricas):
    area = forma.calcular_area()
    print(f"A area da figura {i} - {area[0]} foi de {round(area[1], 2)} m2.")
