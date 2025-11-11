from os import system
import random
from list_utils import maior_numero
system("cls")

numero_lista = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]
print(f"O maior número da lista é: {maior_numero(numero_lista)}")