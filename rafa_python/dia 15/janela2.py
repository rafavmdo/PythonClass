from os import system
system("cls") 

# Para usar esta biblioteca, primeiro instale-a no seu terminal:
# pip install pygame
# Para verificar se a instalação deu certo, digite: pip list
import pygame

pygame.init()

# Para criar uma janela redimensionável, passamos uma flag
TELA = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("Janela Redimensionável")

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        # O evento VIDEORESIZE ocorre quando o usuário muda o tamanho
        if evento.type == pygame.VIDEORESIZE:
            print(f"Janela redimensionada para: {evento.w} x {evento.h}")

pygame.quit()

# Para usar esta biblioteca, primeiro instale-a no seu terminal:
# pip install pygame
# Para verificar se a instalação deu certo, digite: pip list
import pygame

pygame.init()

TELA = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tela Azul")

# Definindo cores com tuplas RGB
PRETO = (0, 0, 0)
AZUL_CEU = (135, 206, 235)


rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # 1. Preenche o fundo da tela com a cor definida
    TELA.fill(AZUL_CEU)

    # 2. Atualiza a tela para exibir o que foi desenhado
    pygame.display.flip()

pygame.quit()

