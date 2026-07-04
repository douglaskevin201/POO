class Pessoa:
    
    def __init__(self, nome, idade):
        '''Inicializa atributos que descrevem uma pessoa'''
        self.nome = nome
        self._idade = idade #Inserido um underscore para indicar atributo francamente privado.
        #Atributo francamente privado deve ser acessado através de metodos de acesso (metodos getters)
    def get_nome(self):
        return self.nome
    
    def get_idade(self):
        return self._idade #Retornando um atributo francamente privado.
    

nova_pessoa = Pessoa('Carlos Alberto', 80)
print(nova_pessoa.nome)
print(nova_pessoa._idade) #Exibindo um atributo francamente privado.
print(nova_pessoa.get_idade()) #Exibindo um atributo francamente privado por meio do método get()
