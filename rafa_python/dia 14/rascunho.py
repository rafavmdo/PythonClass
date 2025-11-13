from os import system
system("cls")
import os

nome_antigo = "rascunho.txt"
nome_novo = "versao_final.txt"

# Verifique se o arquivo 'rascunho.txt' existe antes de rodar.
if os.path.exists(nome_antigo):
    os.rename(nome_antigo, nome_novo)
    print(f"O arquivo '{nome_antigo}' foi renomeado para '{nome_novo}'.")
else:
    print(f"Erro: O arquivo '{nome_antigo}' não foi encontrado.")