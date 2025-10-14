from os import system
system("cls")

altura = float(input("Digite sua altura: "))

if altura >= 1.60:
    print("Entrada permitida")
else:
    print("Sinto muito, sua altura não é suficiente.")