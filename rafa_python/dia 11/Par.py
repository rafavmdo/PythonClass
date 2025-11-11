from os import system
import random
system("cls")

def par(numero):
    if numero % 2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} É impar")

par(random.randint(1, 100))
par(random.randint(1, 100))
par(random.randint(1, 100))
