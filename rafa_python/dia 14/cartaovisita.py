from os import system
system("cls")

nome = input("Digite seu nome: ")
profissao = input("Digite sua profissão: ")
email = input("Digite seu e-mail: ")

with open("cartao.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Nome: " + nome + "\n")
    arquivo.write("Profissão: " + profissao + "\n")
    arquivo.write("E-mail: " + email + "\n")

print("\nCartão de visita salvo em 'cartao.txt'!")