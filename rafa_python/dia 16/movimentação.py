from os import system
system("cls")
# Para usar esta biblioteca, primeiro instale-a no seu terminal:
# pip install pygame
# Para verificar se a instalação deu certo, digite: pip list
import pygame
import random

pygame.init()
TELA = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Movendo com o Teclado")

BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)
COR_ALEATORIA = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))

# jogador 1 

jogador_x, jogador_y = 375, 500
jogador_largura, jogador_altura = 50, 50
jogador1 = pygame.Rect(jogador_x, jogador_y, 50, 50)

# jogador 2

jogador_x2, jogador_y2 = 375, 500
jogador_largura2, jogador_altura2 = 50, 50
jogador2 = pygame.Rect(jogador_x2, jogador_y2, 50, 50)

velocidade = 5
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            COR_ALEATORIA = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))   
    # Pega o estado de todas as teclas
    teclas = pygame.key.get_pressed()
    # rect 1
    if teclas[pygame.K_LEFT] and jogador_x > 0:
        jogador1.x -= velocidade
    if teclas[pygame.K_RIGHT] and jogador_x < 800 - jogador_largura:
        jogador1.x += velocidade
    if teclas[pygame.K_UP] and jogador_y > 0:
        jogador1.y -= velocidade
    if teclas[pygame.K_DOWN] and jogador_y < 600 - jogador_altura:
        jogador1.y += velocidade
    # rect 2

    if teclas[pygame.K_a] and jogador_x2 > 0:
        jogador2.x -= velocidade
    if teclas[pygame.K_d] and jogador_x2 < 800 - jogador_largura2:
        jogador2.x += velocidade
    if teclas[pygame.K_w] and jogador_y2 > 0:
        jogador2.y -= velocidade
    if teclas[pygame.K_s] and jogador_y2 < 600 - jogador_altura2:
        jogador2.y += velocidade

    if jogador1.colliderect(jogador2):
        AZUL = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))

    
    TELA.fill(BRANCO)
    pygame.draw.rect(TELA, AZUL, (jogador1))
    pygame.draw.rect(TELA, COR_ALEATORIA, (jogador2))
    pygame.display.flip()


pygame.quit()