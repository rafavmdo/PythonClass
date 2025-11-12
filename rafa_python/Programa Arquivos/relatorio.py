from os import system
system("cls")

# # Arquivo: relatorio.py
# print("Gerando o relatório de vendas...")

# # O modo 'w' cria um novo arquivo. Se ele já existir, o conteúdo antigo será APAGADO.
# with open("relatorio_de_vendas.txt", "w", encoding="utf-8") as arquivo:
#     # O método .write() escreve o texto que passamos para ele.
#     arquivo.write("Relatório de Vendas - 21 de Agosto de 2025\n")
#     arquivo.write("=" * 40 + "\n") # Escreve uma linha decorativa
#     arquivo.write("Produto A: 15 unidades vendidas\n")
#     arquivo.write("Produto B: 8 unidades vendidas\n")
#     arquivo.write("Produto C: 22 unidades vendidas\n")

# print("Arquivo 'relatorio_de_vendas.txt' gerado com sucesso!")


# # Arquivo: resumo.py

# # --- Parte 1: Lendo o arquivo existente ---
# print("--- Conteúdo Atual do Relatório ---")
# try:
#     with open("relatorio_de_vendas.txt", "r", encoding="utf-8") as arquivo_leitura:
#         conteudo = arquivo_leitura.read()
#         print(conteudo)
# except FileNotFoundError:
#     print("O arquivo de relatório ainda não existe! Rode o primeiro exemplo.")

# # --- Parte 2: Adicionando conteúdo ao final do arquivo ---
# print("\nAdicionando resumo ao final do relatório...")
# # O modo 'a' abre o arquivo e posiciona o cursor no final, para não sobrescrever.
# with open("relatorio_de_vendas.txt", "a", encoding="utf-8") as arquivo_escrita:
#     arquivo_escrita.write("\n--- Resumo ---\n")
#     arquivo_escrita.write("Total de 45 unidades vendidas.\n")

# print("Resumo adicionado com sucesso!")