from os import system as limpar
limpar("cls")

# Exemplo 1: Menu de Jogo
opcao = input("Escolha sua classe (1-Guerreiro, 2-Mago, 3-Arqueiro): ")

match opcao:
    case '1':
        print("Você escolheu a classe Guerreiro! \U00002694")
        print("Força e resistência são seus pontos fortes.")
    case '2':
        print("Você escolheu a classe Mago! \U0001F52E")
        print("O poder arcano está ao seu dispor.")
    case '3':
        print("Você escolheu a classe Arqueiro! \U0001F3F9")
        print("Precisão e agilidade são suas marcas.")
    case _: # Caso padrão
        print("Opção inválida! Escolha um número de 1 a 3.")