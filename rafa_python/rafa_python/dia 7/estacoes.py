from os import system as limpar
limpar("cls")

estacao = input("Digite uma estação do ano: ")
match estacao:
    case "verao":
        print("é recomendável roupas leves e protetor solar, perfeito para ir à praia!")
    case "inverno":
        print("é recomendável roupas quentes para te aquecer.")
    case "outono":
        print("é recomendável roupas confortáveis de tons neutros.")
    case "primavera":
        print("é recomendável roupas leves e confortáveis.")
    case _:
        print("Você não inseriu uma estação do ano.")