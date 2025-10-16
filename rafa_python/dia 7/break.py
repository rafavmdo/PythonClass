from os import system as limpar
limpar("cls")

# Exemplo 1: Usando 'break' para sair de um menu
# Este loop seria infinito se não fosse pelo 'break'.
while True:
    opcao = input("Digite 'sair' para terminar o programa: ").lower()
    if opcao == 'sair':
        print("Entendido! Encerrando o programa...")
        break # Sai imediatamente do loop while
    print(f"Você digitou: {opcao}. Tente de novo.")
print("Fim")