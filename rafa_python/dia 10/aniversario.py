from os import system
import time
system("cls")

print("Olá! Seja bem-vindo ao aniversário do kenneth!\n\nDigite seu nome abaixo para a confirmação de\nsua entrada, por questões de segurança.")
nome = ""
convidados = []
##############################################################################
for i in range(30):
    nome = input("\n Nome: ")
    
    if nome.lower() != "12345":
        system("cls")
        print("Processando...")
        time.sleep(1)
        convidados.append(nome)
        print("Olá! Seja bem-vindo ao aniversário do kenneth!\n\nDigite seu nome abaixo para a confirmação de\nsua entrada, por questões de segurança.\n ")
        print(f"Convidados: {len(convidados)}")
    else:
        system("cls")
        break
convidados.sort()
system("cls")
print(f"Total de convidados: {len(convidados)}\n(convidados)")