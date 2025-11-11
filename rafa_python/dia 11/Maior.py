from os import system
import random
system("cls")

def maior(n1, n2):
    if n1 > n2:
        print(f"{n1} é maior que {n2}")
    else:
        print(f"{n2} é maior que {n1}")

maior(random.randint(1, 50), random.randint(1, 50))
maior(random.randint(1, 50), random.randint(1, 50))
maior(random.randint(1, 50), random.randint(1, 50))