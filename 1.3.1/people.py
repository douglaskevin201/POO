
class Pessoa:

    def __init__(self, nome, idade):

        self.nome = nome
        self.__idade - idade #Inserido dois underscore para indicar atributo fortemente privado.

    def get_nome(self):
        return self.nome
    
    def get_idade(self):
        return self.__idade #Retornando um atributo fortemente privado
    
    nova_pessoa = Pessoa('Carlos Alberto', 80)
    print(nova_pessoa.nome)
    print(f'Idade = {nova_pessoa.get_idade()}') #Exibindo um atributo fortemente privado
    print(nova_pessoa._Pessoa__idade) #Exibindo um atributo fortemente privado por meio da classe 
    
    
