from os import system 
system("cls")

resultado = 12 * 5

palpite = int(input("Quanto é 12 * 5?\nDigite sua resposta: "))

acertou = palpite == resultado


if palpite == resultado:
    print(f"Acertou!\n{acertou}")
else:
    print(f"incorreto! o resultado correto é {resultado}.")