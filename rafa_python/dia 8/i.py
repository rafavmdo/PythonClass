# Este é um laço "for", usado para repetir um bloco de código várias vezes.
# Aqui, ele vai percorrer os números de 0 até 9 (10 não entra, pois o range para antes).

for i in range(10):  
    # A cada repetição, a variável "i" assume um valor do intervalo gerado por range(10).
    # O range(10) gera a sequência: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

    # Este comando imprime o valor atual de "i" formatado dentro de uma string.
    # A letra "f" antes das aspas indica uma f-string, usada para inserir variáveis dentro do texto.
    print(f"O valor de i é {i}")