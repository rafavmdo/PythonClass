from os import system
system("cls")

numeros = [42, 15, 99, 56, 8, 23]
print(f"Lista de números: {numeros}")

menor_numero = min(numeros)
maior_numero = max(numeros)

print(f"O menor número da lista é: {menor_numero}")
print(f"O maior número da lista é: {maior_numero}")

numeros.sort()
print(f"Lista ordenada: {numeros}")