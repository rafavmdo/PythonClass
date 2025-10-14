from os import system
system("cls")

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Ingresso para o filme de terror liberado")
elif idade <= 18:
    print("Você não possui a idade necessária. \nIngresso bloqueado.")
