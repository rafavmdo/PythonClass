from os import system
system("cls")
# Para usar esta biblioteca, primeiro instale-a no seu terminal:
# pip install pygame
# Para verificar se a instalação deu certo, digite: pip list
import pygame

pygame.init()
TELA = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Desenhando Formas")

BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    TELA.fill(BRANCO)

    # Desenha um retângulo vermelho em (x, y, largura, altura)
    pygame.draw.rect(TELA, VERMELHO, (100, 150, 80, 50))

    # Desenha um círculo verde em (x, y), com raio 40
    pygame.draw.circle(TELA, VERDE, (400, 300), 40)

    pygame.display.flip()

pygame.quit()