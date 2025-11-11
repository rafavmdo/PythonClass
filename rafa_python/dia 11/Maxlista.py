from os import system
import random
system("cls")


def maior_numero(lista):
    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior
numeros = [random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100)]
print(f"O maior número da lista:\n{numeros}\n\nÉ {maior_numero(numeros)}")