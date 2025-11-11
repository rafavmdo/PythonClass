from os import system
system("cls")

def contar_vogais(palavra):
    vogais = "aeiou"
    contagem = 0
    for letra in vogais:
        for letra in palavra:
            contagem += 1
    return contagem
texto = input("Sua palavra:\n-> ")
print(f"Número de vogais na frase \"{contar_vogais(texto)}\"")