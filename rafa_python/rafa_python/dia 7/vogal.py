from os import system as limpar
limpar("cls")

letra = input("Digite uma letra: ")
match letra:
    case 'a'|'e'|'i'|'o'|'u':
        print("A letra inserida é uma vogal")
    case _: 
        print("A letra inserida é uma consoante")