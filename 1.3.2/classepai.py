class ClassePai:
    def __init__(self, atributo):
        self.atributo = atributo
    def metodo_pai(self):
        return "Metodo da classe pai"
    
class ClasseFilha(ClassePai):
    def __init__(self,atributo,novo_atributo):
        super().__init__(atributo) #chama construtor da classe pai
        self.novo_atributo = novo_atributo
    def metodo_filha(self):
        return "Metodo da classe filha"


obj = ClasseFilha("valor1", "valor2")
print(obj.metodo_pai()) #herdado da classe pai
print(obj.metodo_filha()) #proprio da classe filha 
