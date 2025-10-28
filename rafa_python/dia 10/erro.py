numeros = (10, 20, 30, 40)

# A linha abaixo vai causar um erro, pois tuplas são imutáveis.
# É importante que o aluno veja o erro acontecer para entender o conceito.
# Para o código rodar, comente a linha abaixo com um #
numeros[0] = 5

# O erro será: TypeError: 'tuple' object does not support item assignment