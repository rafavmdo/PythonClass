from os import system 
system("cls") 

numero = int(input("Digite um número inteiro: "))
par = (numero % 2) == 0

print(f"O número {numero} é par? {par}")