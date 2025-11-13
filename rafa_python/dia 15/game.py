from os import system
system("cls")
import pygame
# Para usar esta biblioteca, primeiro instale-a no seu terminal:
# pip install pygame
# Para verificar se a instalação deu certo, digite: pip list

# 1. Inicializar o pygame
pygame.init()

# 2. Definir as dimensões da tela
largura, altura = 800, 600
TELA = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Minha Primeira Janela")

# 3. Loop principal do jogo
rodando = True
while rodando:
    # 4. Checar eventos (ações do usuário)
    for evento in pygame.event.get():
        # Se o evento for de fechar a janela
        if evento.type == pygame.QUIT:
            rodando = False

# 5. Finalizar o pygame
pygame.quit()

