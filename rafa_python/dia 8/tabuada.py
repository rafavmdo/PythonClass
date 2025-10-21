from os import system
system("cls")

numero = int(input("Qual tabuada você quer ver? "))

print(f"\nTabuada do {numero}")

for i in range(11):
    print(f"{numero} x {i} = {numero * i}")