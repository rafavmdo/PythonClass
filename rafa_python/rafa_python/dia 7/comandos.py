from os import system as limpar
limpar("cls")

opcao = input("Digite um comando: \n1. Entrar\n2. Sair\n3. Ajuda\n\n\t-> ").lower()
match opcao:
    case "entrar":
        print("Seja bem-vindo")
    case "sair":
        print("Volte logo!")
    case "ajuda":
        print("Olá! com o que posso te ajudar?")
    case _:
        print("Informação inválida")