# Exemplo 1 - uso do os.getcwd() para adquirir o
# caminho da pasta atual

# import os

# caminho = os.getcwd()
# # Imprime o caminho da pasta atual
# print(f"O caminho da pasta atual é: {caminho}")


# Exemplo 2 - uso do os.getcwd() para adquirir o
# caminho da pasta atual e inserir novos caminho
# de subpastas para uso no projeto

# import os

# # Pega a pasta atual de execução
# pasta_atual = os.getcwd()
# print("Pasta atual:", pasta_atual)

# # Cria o caminho completo até assets/sounds
# caminho_sons = os.path.join(pasta_atual, "assets", "sounds")
# print("Caminho da pasta de sons:", caminho_sons)

# Exemplo de arquivo dentro da subpasta
# arquivo_som = os.path.join(caminho_sons, "beep.wav")
# print("Arquivo de som:", arquivo_som)
