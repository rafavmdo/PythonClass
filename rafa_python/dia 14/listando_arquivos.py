from os import system
system("cls")
import os

conteudo_diretorio = os.listdir('.')

print("--- Conteúdo do Diretório Atual ---")
for item in conteudo_diretorio:
    print(item)