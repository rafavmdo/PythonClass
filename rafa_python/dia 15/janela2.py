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