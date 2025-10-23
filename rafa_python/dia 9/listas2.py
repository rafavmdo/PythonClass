from os import system
system("cls")

animais = ["cachorro", "gato", "coelho"]
print("Lista original:", animais)
animais.append("papagaio")
print("Lista atualizada:", animais)
print("-" * 100)
################################################################
paises = ["Peru", "Chile", "Argentina", "Uruguai"]
paises.insert(1, "Brasil")
print(paises)
print("-" * 100)
#################################################################
numeros = [10, 20, 30, 40, 50]
print("Tamanho inicial:", len(numeros))
numeros.append(60)
print("Tamanho após adicionar:", len(numeros))
print("-" * 100)
#################################################################
alunos = ["Rafaela", "Mariana", "Lorena", "Anyke", "Eluara", "Kenneth"]
print("Antes:", alunos)
del alunos[2]
print("Depois:", alunos)
print("-" * 100)
###################################################################
compras = []
compras.append("mochila")
compras.append("livro")
compras.append("estojo")
compras.insert(0,"garrafa")
print(f"Lista original: {compras}")
print(f"Tamanho da lista:  {len(compras)}")
print(f"Item removido: {compras[1]}")
del compras[1]
print(f"Lista atualizada: {compras}")
print("-" * 100)
#####################################################################