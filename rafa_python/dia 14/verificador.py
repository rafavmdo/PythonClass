from os import system
system("cls")
import os

nome = input("Digite o nome de um arquivo ou pasta para verificar: ")
if os.path.exists(nome):
    print(f"Sim, '{nome}' existe no diretório atual.")
else:
    print(f"Não, '{nome}' não foi encontrado no diretório atual.")