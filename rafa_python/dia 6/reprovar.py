from os import system
system("cls")

nota = float(input("Digite sua nota: "))

if nota >= 7.0:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado.")