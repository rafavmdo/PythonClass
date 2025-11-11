def contar_vogais(palavra):
    vogais = "aeiouAEIOU"
    contagem = 0
    for letra in palavra:
        if letra in vogais:
            contagem += 1
    return contagem
    
def inverter_string(texto):
    return texto[::-1]