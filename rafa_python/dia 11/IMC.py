from os import system
system("cls")

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    print(f"Seu IMC é {imc:.2f}")

v1 = float(input("Digite seu peso: "))
v2 = float(input("Digite sua altura: "))

calcular_imc(v1, v2)