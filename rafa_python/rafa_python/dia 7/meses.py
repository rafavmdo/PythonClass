from os import system as limpar
limpar("cls")

mes = int(input("Digite o número de um mês: "))

match mes:
    case 1:
        print("Janeiro")
    case 2:
        print("Fevereiro")
    case 3:
        print("Março")
    case _:
        print("Número inválido")