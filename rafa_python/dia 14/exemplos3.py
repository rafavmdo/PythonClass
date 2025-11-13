# # Exemplo com os.mkdir()

# import os
# nome_da_pasta = "meus_relatorios"
# if not os.path.exists(nome_da_pasta):
#     os.mkdir(nome_da_pasta)
#     print(f"A pasta '{nome_da_pasta}' foi criada.")

# -----------------------------------------------------------
# # Exemplo com os.remove()

# obs: Deleta um arquivo permanentemente. 
# MUITO CUIDADO: Esta ação não pode ser desfeita e o arquivo não vai para a lixeira!!!!!!!!

# import os
# if os.path.exists("copia_de_seguranca.txt"):
#     os.remove("copia_de_seguranca.txt")
#     print("A cópia de segurança foi removida.")

#----------------------------------------------------------------
# Exemplo com os.listdir()
# obs: '.' significa o diretório atual
# obs: Retorna uma lista com os nomes de todos os arquivos e subpastas dentro de um diretório.

# import os
# print("\nConteúdo da pasta atual:")
# print(os.listdir('.'))


