from os import system as limp
limp("cls")

# Lê o arquivo já existente. 
# Se não existir o arquivo o sistema retorna o erro 
# FileNotFoundError
with open("dados.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

    # Exemplo com modo 'w'
# Este código vai criar o arquivo 'lista_de_frutas.txt' ou apagar o que já existia.
# with open("dados.txt", "w", encoding="utf-8") as arquivo:
#     arquivo.write("Teste1\n") # O \n cria uma nova linha
#     arquivo.write("Teste2\n")
#     arquivo.write("Teste2\n")

# print("Arquivo 'dados.txt' foi criado/sobrescrito com sucesso!")
# print()

# Exemplo com modo 'a'
# Vamos adicionar mais frutas ao arquivo que acabamos de criar.
with open("dados.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("Teste4\n")
    arquivo.write("Teste5\n")

print("Novas frutas foram adicionadas ao final do arquivo!")