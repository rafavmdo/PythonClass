from os import system
system("cls")

frutas = ["Maçã", "Banana", "Laranja"]

print("Escolha uma fruta pelo número:")
print("0: Maçã")
print("1: Banana")
print("2: Laranja")

try:
    posicao_texto = input("Digite o número da sua escolha: ")
    posicao = int(posicao_texto)
    fruta_escolhida = frutas[posicao]
    print(f"Você escolheu: {fruta_escolhida}!")

except:
    print("Posição inválida! Escolha 0, 1 ou 2.")