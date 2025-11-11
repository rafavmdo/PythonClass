from os import system
system("cls")
import requests

cep = input("Digite o CEP para consulta: ")
url = "https://viacep.com.br/ws/" + cep + "/json/"

resposta = requests.get(url)
dados = resposta.json()

print(f"\nlogradouro: {dados['logradouro']}")
print(f"cidade: {dados['localidade']}")