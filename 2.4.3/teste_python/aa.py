import random

def sortear_computador():
    return random.choice(['pedra', 'papel', 'tesoura'])

escolha = input("Escolha pedra, papel ou tesoura: ").lower()
computador = sortear_computador()
print(f"Computador escolheu: {computador}")
print(f"Voce escolheu: {escolha}")
if escolha == computador:
    print("Empate!")
elif (escolha == 'pedra' and computador == 'tesoura') or \
     (escolha == 'papel' and computador == 'pedra') or \
     (escolha == 'tesoura' and computador == 'papel'):
    print("Voce ganhou!!")
else:
    print("Computador ganhou!!!")
    