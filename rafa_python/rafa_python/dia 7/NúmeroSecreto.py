import random
import time
from os import system as limpar
limpar("cls")

numerosecreto = random.randint(100, 500)
tentativa = int(input("Tente adivinhar o número secreto:\n- "))
tentativas = 1

while tentativa != numerosecreto:
    if tentativa > numerosecreto:
        limpar("cls")
        print("Número incorreto.")
        print(f"Tentativas: {tentativas}")
        print(f"Número adivinhado: {tentativa}")
        time.sleep(1)
        print("")
        print("O número secreto é menor do que a sua tentativa.")
        print("")
        time.sleep(1)
        tentativa = int(input("Tente adivinhar novamente o número secreto:\n- "))
        tentativas += 1
    else:
        limpar("cls")
        print("Número incorreto.")
        print(f"Tentativas: {tentativas}")
        print(f"Número adivinhado: {tentativa}")
        time.sleep(1)
        print("")
        print("O número secreto é maior do que a sua tentativa.")
        print("")
        time.sleep(1)
        tentativa = int(input("Tente adivinhar novamente o número secreto:\n- "))
        tentativas += 1
print("Parabens! Você adivinhou o número secreto.")