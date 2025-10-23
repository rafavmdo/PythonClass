from os import system
system("cls")

notas = [7.5, 8.0, 9.5, 6.0, 10.0]
soma_das_notas = 0.0
for nota in notas:
    soma_das_notas = soma_das_notas + nota
print(f"A lista de notas é: {notas}")
print(f"A soma total das notas é: {soma_das_notas}")