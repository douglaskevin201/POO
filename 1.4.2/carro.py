class Carro:
    """Uma tentativa simples de representar um carro"""
    def __init__(self, fabricante, modelo, ano):
        """inicializa os atributos que descrevem um carro.
        leitura_hodometro valor constante inicial"""
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano
        self.leitura_hodometro = 0
        self.tanque = 0 # Criado para armazenar abastecimento do tanque. Default 0 litros

    def buscar_nome_descricao(self):
        """Devolve um nome descritivo, em formato elegante"""
        nome_extenso = str(self.ano) + ' ' + self.fabricante + ' ' + self.modelo
        return nome_extenso.title()
    
    def ler_hodometro(self):
        """exibe uma frase que mostra a milhagem do carro"""
        print("Esse carro tem " + str(self.leitura_hodometro)+ " milhas.")

    def atualizar_hodometro(self, milhas):
        """define o valor da leitura do hodometro com o valor especificado 
            rejeita a mudança se for uma tentativa de definir um valor menor para o hodometro"""
        
        if milhas >= self.leitura_hodometro:
            self.leitura_hodometro = milhas
        else:
            print("Você esta tentando reduzir o valor do hodometro !")

    def abastecer_tanque(self, tanque):
        self.tanque = tanque 
        print("Tanque atualizado para " + str(self.tanque) + " litros.")

# Definição da classe CarroEletrico que herda da classe Carro
class CarroEletrico(Carro):
    """Representa aspectos de um carro especifico de veiculos elétricos"""
    def __init__(self, fabricante, modelo, ano):
        super().__init__(fabricante, modelo, ano)
        self.bateria = Bateria() # Modificado aqui de self.bateria = 70 para self.bateria = Bateria()

    def abastecer_tanque(self):
        print("Esse Modelo de carro nao possui tanque!")


# Definição da classe Bateria que se relaciona com a classe CarroEletrico
class Bateria:
    """Uma tentativa simples de modelar uma bateria para um carro eletrico"""
    def __init__(self, tamanho_bateria=70):
        self.tamanho_bateria = tamanho_bateria

    def descricao_bateria(self):
        print("Esse carro tem " + str(self.tamanho_bateria) + "KWH de capacidade")


    def buscar_faixa(self):
        """Exibe uma frase sobre a distancia que o carro é capaz de percorrer de acordo
        com as especificações da bateria"""
        if self.tamanho_bateria == 70:
            range = 240
        elif self.tamanho_bateria == 85:
            range = 270
        message = "Esse carro pode percorrer aproximadamente " + str(range)
        message += " milhas com a bateria cheia."
        print(message)


# Utilizando as classes Carro, CarrosEletricos e Bateria

meu_novo_carro_teste = Carro('Honda', 'New Civic', 2020)
print(meu_novo_carro_teste.buscar_nome_descricao())
meu_novo_carro_teste.ler_hodometro()
meu_novo_carro_teste.atualizar_hodometro(2000)
meu_novo_carro_teste.ler_hodometro()
meu_novo_carro_teste.abastecer_tanque(40)

meu_eletrico = CarroEletrico('tesla', 'model s', 2016)
print(meu_eletrico.buscar_nome_descricao())
meu_eletrico.bateria.buscar_faixa()
meu_eletrico.bateria.tamanho_bateria = 90
meu_eletrico.bateria.descricao_bateria()
meu_eletrico.abastecer_tanque()


