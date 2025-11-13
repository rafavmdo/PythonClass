from os import system
system("cls")

with open("desejos.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Minha lista de desejos:\n")

novo_desejo = input("Digite um desejo para adicionar à lista: ")

with open("desejos.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(novo_desejo + "\n")

print("Seu desejo foi adicionado à lista!")