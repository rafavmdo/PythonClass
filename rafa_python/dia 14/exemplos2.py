# # Exemplo com os.rename()
# # Primeiro, vamos garantir que o arquivo a ser renomeado exista
# with open("arquivo_antigo.txt", "w") as f:
#     f.write("Este arquivo será renomeado.")
#     import os
# # Agora, renomeamos com segurança
# if os.path.exists("arquivo_antigo.txt"):
#     os.rename("arquivo_antigo.txt", "arquivo_novo.txt")
#     print("O arquivo foi renomeado com sucesso.")