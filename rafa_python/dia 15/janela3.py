# Para usar esta biblioteca, primeiro instale-a no seu terminal:
# pip install pygame
# Para verificar se a instalação deu certo, digite: pip list
import pygame
import random

pygame.init()
TELA = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Clique para Mudar a Cor")

# Função para gerar uma cor aleatória
def cor_aleatoria():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

cor_fundo = cor_aleatoria()

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        # Checa se o evento foi um clique do mouse
        if evento.type == pygame.MOUSEBUTTONDOWN:
            cor_fundo = cor_aleatoria()
            print(f"Nova cor de fundo: {cor_fundo}")

    TELA.fill(cor_fundo)
    pygame.display.flip()

pygame.quit()
