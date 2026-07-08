class Animal:
    def __init__(self, apelido):
        print(f"classe animal: {apelido}")


class Mamifero(Animal):
    def __init__(self, apelido):
        print(f"classe mamifero: {apelido}")
        super().__init__(apelido)


class NaoVoadores(Mamifero):
    def __init__(self, apelido):
        print(f"Classe Nao Voadores: {apelido}")
        super().__init__(apelido)


class Naoaquaticos(Mamifero):
    def __init__(self, apelido):
        print(f"Classe Nao aquaticos: {apelido}")
        super().__init__(apelido)

class Dog(Naoaquaticos, NaoVoadores):
    def __init__(self, apelido):
        print(f"Classe Nao voadores e Nao aquaticos: {apelido}")
        super().__init__(apelido)

class Voadores(Naoaquaticos):
    def __init__(self, apelido):
        print(f"Classe Voadores: {apelido}")
        super().__init__(apelido)


cachorro = Dog("Rex")
passaro = Voadores("Morcego")


