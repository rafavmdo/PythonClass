from os import system as limpar
limpar("cls")

# Exemplo 2: Usando 'continue' para imprimir apenas números ímpares
contador = 0
while contador < 10:
    contador += 1 # Incrementa o contador
    # Se o número for par...
    if (contador % 2) == 0:
        continue # ...pula o resto do código e vai para a próxima volta
    
    # Este print só é executado para números ímpares
    print(contador)