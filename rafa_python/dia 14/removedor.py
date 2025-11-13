from os import system
system("cls")
import os

arquivo_para_deletar = input("Qual arquivo você deseja deletar? ")

if os.path.exists(arquivo_para_deletar):
    os.remove(arquivo_para_deletar)
    print(f"O arquivo '{arquivo_para_deletar}' foi deletado.")
else:
    print(f"O arquivo '{arquivo_para_deletar}' não foi encontrado.")