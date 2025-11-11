from os import system
import text_utils
system("cls")

palavra = input("Digite sua palavra: ")
vogais = text_utils.contar_vogais(palavra)
invertida = text_utils.inverter_string(palavra)
print(f"\nNa sua frase tem {vogais} vogais")
print(f"Sua frase invertida é: {invertida}")