from os import system
system("cls")

nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))
salario = float(input("Informe seu salário: "))
status = bool(input("Status de login (True/False): "))
system("cls")

print(f"Nome: {nome}\nIdade: {idade}\nSalário: {salario}\nStatus: {status}")