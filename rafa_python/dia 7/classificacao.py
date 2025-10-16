from os import system as limpar
limpar("cls")

import random

posicao = random.randint(1, 10)
print(f"sua posicao foi: {posicao}º lugar")
match posicao:
    case 1:
        print("Ouro!!")
    case 2:
        print("Prata!!")
    case 3:
        print("Bronze!!")
    case _:
        print("Sem medalhas dessa vez...")
