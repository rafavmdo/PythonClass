from os import system
system("cls")
pessoas_texto = input("Quantas pessoas estão na sala? ")

try:
    numero_pessoas = int(pessoas_texto)
    resultado = 100 / numero_pessoas
    print(f"Cada pessoa recebe {resultado:.2f} partes.")

except:
    print("Não é possível dividir por zero pessoas!")