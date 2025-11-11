from os import system
system("cls")
import requests

url = "https://viacep.com.br/ws/14165486/json/"

resposta = requests.get(url)
dados = resposta.json()

# Acessando um item do dicionário
print(f"Bairro: {dados}")