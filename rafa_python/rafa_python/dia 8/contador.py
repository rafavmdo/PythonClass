from os import system
system("cls")

frase = input("Digite uma frase: ").lower()
letra_procurada = input("Qual letra você quer contar? ").lower()
contador = 0

for letra in frase:
    if letra == letra_procurada:
        contador += 1 
print(f"A letra '{letra_procurada}' aparece {contador} vezes na frase.")