from os import system
system("cls")

entrada_usuario = input("Digite um número inteiro: ")

try:
    numero = int(entrada_usuario)
    print(f"Ótimo! O número {numero} é um inteiro válido.")

except:
    print("Erro: Por favor, digite um número inteiro válido.")