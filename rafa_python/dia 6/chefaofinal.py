from os import system
system("cls")

import random



jogada_computador = ["pedra", "papel", "tesoura"]
decisao = random.randrange (jogada_computador)
jogada_usuario = input("Sua jogada (pedra, papel, tesoura): ").lower()

print(f"\nO computador escolheu: {jogada_computador}")
print(f"Você escolheu: {jogada_usuario}")

# Lógica do jogo
if jogada_usuario == decisao:
    print("Resultado: Empate!")
elif (jogada_usuario == "pedra" and jogada_computador == "tesoura") or \
     (jogada_usuario == "tesoura" and jogada_computador == "papel") or \
     (jogada_usuario == "papel" and jogada_computador == "pedra"):
    print("Resultado: Você venceu! \U0001F3C6")
else:
    print("Resultado: O computador venceu! \U0001F916")