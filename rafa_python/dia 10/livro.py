from os import system
system("cls")

livro = {
    "titulo": "Noiva",
    "autor": "Ali Hazelwood",
    "ano": 2024
}

print("Informações do Livro:")
print(livro)
#############################################
print(f"O autor do livro é: {livro['autor']}")
############################################
livro["genero"] = "Romantasia"
print("Dicionário atualizado:")
print(livro)