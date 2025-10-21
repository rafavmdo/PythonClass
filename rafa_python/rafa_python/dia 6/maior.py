from os import system
system("cls")

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

if num1 > num2:
    print(f"O número {num1} é maior que o número {num2}.")
elif num2 > num1:
    print(f"O número {num2} é maior que o número {num1}.")
else:
    print("Os dois números são iguais.")