# Exemplo 1: Login com verificação em duas etapas
usuario_correto = True
senha_correta = False

# O primeiro 'if' verifica o usuário
if usuario_correto:
    print("Usuário correto. Agora, verifique a senha.")
    

    if senha_correta:
        print("Senha correta. Acesso concedido!")
    else:
        print("Senha incorreta. Acesso negado.")
else:
    print("Usuário não encontrado.")