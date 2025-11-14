# main.py - Código Completo do Jogo da Cobrinha
from os import system
system("cls")
import pygame
import random

pygame.init()

# Definições da tela
LARGURA, ALTURA = 600, 400
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da Cobrinha")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)

# Cobra e Comida
TAMANHO_BLOCO = 20
VELOCIDADE = 15

relogio = pygame.time.Clock()
fonte = pygame.font.Font(None, 35)

def desenha_cobra(tamanho_bloco, lista_cobra):
    for x in lista_cobra:
        pygame.draw.rect(TELA, PRETO, [x[0], x[1], tamanho_bloco, tamanho_bloco])

def mensagem(msg, cor):
    texto = fonte.render(msg, True, cor)
    TELA.blit(texto, [LARGURA / 10, ALTURA / 3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = LARGURA / 2
    y1 = ALTURA / 2
    x1_change = 0
    y1_change = 0

    lista_cobra = []
    comprimento_cobra = 1

    comida_x = round(random.randrange(0, LARGURA - TAMANHO_BLOCO) / TAMANHO_BLOCO) * TAMANHO_BLOCO
    comida_y = round(random.randrange(0, ALTURA - TAMANHO_BLOCO) / TAMANHO_BLOCO) * TAMANHO_BLOCO

    while not game_over:

        while game_close:
            TELA.fill(BRANCO)
            mensagem("Você Perdeu! Pressione C para jogar de novo ou Q para sair", VERMELHO)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -TAMANHO_BLOCO
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = TAMANHO_BLOCO
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -TAMANHO_BLOCO
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = TAMANHO_BLOCO
                    x1_change = 0

        if x1 >= LARGURA or x1 < 0 or y1 >= ALTURA or y1 < 0:
            game_close = True
        
        x1 += x1_change
        y1 += y1_change

        TELA.fill(BRANCO)
        pygame.draw.rect(TELA, VERDE, [comida_x, comida_y, TAMANHO_BLOCO, TAMANHO_BLOCO])
        
        cabeca_cobra = []
        cabeca_cobra.append(x1)
        cabeca_cobra.append(y1)
        lista_cobra.append(cabeca_cobra)
        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]

        for x in lista_cobra[:-1]:
            if x == cabeca_cobra:
                game_close = True

        desenha_cobra(TAMANHO_BLOCO, lista_cobra)
        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, LARGURA - TAMANHO_BLOCO) / TAMANHO_BLOCO) * TAMANHO_BLOCO
            comida_y = round(random.randrange(0, ALTURA - TAMANHO_BLOCO) / TAMANHO_BLOCO) * TAMANHO_BLOCO
            comprimento_cobra += 1

        relogio.tick(VELOCIDADE)

    pygame.quit()

gameLoop()