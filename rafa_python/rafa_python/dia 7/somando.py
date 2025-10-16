from os import system as limpar
limpar("cls")

numero = int(input("Digite um número para a soma\n- "))
soma = 0

while numero != 0:
    limpar("cls")
    soma = numero + soma
    print(f"Soma: {soma}")
    numero = int(input("Digite um número para a soma:\n- "))
print(f"Soma total: {soma}")