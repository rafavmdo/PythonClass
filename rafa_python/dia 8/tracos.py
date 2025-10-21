from os import system
system("cls")

palavra = input("Digite uma palavra: ")
for letra in palavra:
    print(letra + "-", end="")
print("\b ")