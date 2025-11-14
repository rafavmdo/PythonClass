# logica_raid.py (MODIFICADO)
import random
from config_raid import *

def checa_colisao_retangulos(r1, r2):
    return (r1['x'] < r2['x'] + r2['largura'] and
            r1['x'] + r1['largura'] > r2['x'] and
            r1['y'] < r2['y'] + r2['altura'] and
            r1['y'] + r1['altura'] > r2['y'])

class LogicaRaid:
    def __init__(self):
        self.resetar_jogo()

    def resetar_jogo(self):
        self.jogador = {'x': LARGURA_TELA / 2 - 25, 'y': ALTURA_TELA - 60, 'largura': 50, 'altura': 30}
        self.lasers_jogador = []
        self.inimigos = []
        self.pontuacao = 0
        self.game_over = False
        self.timer_inimigo = 0

    def mover_jogador(self, dx):
        self.jogador['x'] += dx
        if self.jogador['x'] < 0: self.jogador['x'] = 0
        if self.jogador['x'] + self.jogador['largura'] > LARGURA_TELA:
            self.jogador['x'] = LARGURA_TELA - self.jogador['largura']

    def jogador_atira(self):
        laser = {'x': self.jogador['x'] + self.jogador['largura']/2 - 2, 'y': self.jogador['y'] - 10, 'largura': 4, 'altura': 10}
        self.lasers_jogador.append(laser)
        return 'laser' # Retorna um evento de som

    def gerar_inimigos(self):
        self.timer_inimigo += 1
        if self.timer_inimigo > 50:
            self.timer_inimigo = 0
            if random.random() < 0.5:
                x_pos = random.randint(50, LARGURA_TELA - 50)
                inimigo = {'x': x_pos, 'y': -50, 'largura': 40, 'altura': 40}
                self.inimigos.append(inimigo)

    def mover_elementos(self):
        for laser in self.lasers_jogador[:]:
            laser['y'] -= VELOCIDADE_LASER
            if laser['y'] + laser['altura'] < 0:
                self.lasers_jogador.remove(laser)
        
        for inimigo in self.inimigos[:]:
            inimigo['y'] += VELOCIDADE_SCROLL // 2
            if inimigo['y'] > ALTURA_TELA:
                self.inimigos.remove(inimigo)

    def checar_colisoes(self):
        eventos_som = []
        for laser in self.lasers_jogador[:]:
            for inimigo in self.inimigos[:]:
                if checa_colisao_retangulos(laser, inimigo):
                    self.lasers_jogador.remove(laser)
                    self.inimigos.remove(inimigo)
                    self.pontuacao += 100
                    eventos_som.append('explosao') # Adiciona um evento de som
                    break
        
        for inimigo in self.inimigos:
            if checa_colisao_retangulos(self.jogador, inimigo):
                self.game_over = True
                eventos_som.append('explosao') # Adiciona um evento de som
        
        return eventos_som

    def update(self):
        self.gerar_inimigos()
        self.mover_elementos()
        return self.checar_colisoes()