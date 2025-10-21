from os import system as limpar
limpar("cls")
import random

numero_secreto = random.randint(1, 10)
tentativas = 0
limite_de_tentativas = 3

while tentativas < limite_de_tentativas:
    palpite = int(input("Adivinhe o número secreto: "))

    if palpite == numero_secreto:
        print("Parabéns!!! você acertou!!!")
        break 
    else:
        print("Errado! Tente de novamente.")
        tentativas += 1

if tentativas == limite_de_tentativas:
    print(f"Fim de jogo! Você usou todas as {limite_de_tentativas} tentativas.")