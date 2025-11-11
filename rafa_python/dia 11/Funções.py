from os import system
import random
import time
import math
system("cls")

def clear():
    print("")
    print("-" * 100)
    time.sleep(6)
    system("cls")
def linha():
    print("")
    print("-" * 100)
    print("")

numeros = [random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100), ]

print(f"{numeros}\nO maior número da lista é {max(numeros)}, e o menor número da lista é {min(numeros)}.")

clear()
linha()
def saudacao():
    print("Olá mundo!")
    print("Seja bem-vindo(a) ao Python!")
    time.sleep(1)

saudacao()
saudacao()
clear()
linha()

def tabuadas():
    tabuada1 = random.randint(1,10)
    tabuada2 = random.randint(1,10)
    for i in range(11):
        print(f"{tabuada1} x {i} == {tabuada1 * i}")

tabuadas()
clear()
linha()

def rolar_dado():
    numero_dado = random.randint(1, 6)
    print("Você joga um dado...")
    time.sleep(1)
    print(f"Caiu o número {numero_dado}.")

rolar_dado()
clear()
linha()

def potencia():
    math.pow(2, 10)

potencia()
clear()
linha()
