from os import system
system("cls")

# frase_filme = input("Digite uma frase do seu filme favorito: ")

# with open("filme_favorito.txt", "w", encoding="utf-8") as arquivo:
#     arquivo.write(frase_filme)

# print("Frase salva com sucesso em 'filme_favorito.txt'!")

with open("filme_favorito.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print("\n--- Frase do seu filme favorito ---")
    print(conteudo)