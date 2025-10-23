from os import system
system("cls")


convidados = ["Kenneth", "Caetano", "Rafaela"]
print(f"Lista inicial: {convidados}")
convidados.insert(0, "Arthur")
print(f"Lista com novo convidado: {convidados}")
#ordem alfabetica:
convidados.sort()
print(f"Lista final ordenada: {convidados}")