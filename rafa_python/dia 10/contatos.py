from os import system
system("cls")

contato = {
    "nome": "Kenneth",
    "telefone": "16 99779-6595"
}

tem_email = "email" in contato
print(f"O contato possui a chave 'email'? {tem_email}")