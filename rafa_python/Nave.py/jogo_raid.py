# jogo_raid.py (MODIFICADO)
import pygame
import sys
from config_raid import *
from logica_raid import LogicaRaid
from placar_raid import carregar_scores, adicionar_score
from sons import gerar_som_laser, gerar_som_explosao # Importa nossa fábrica de sons

class JogoRaid:
    def __init__(self):
        pygame.init()
        pygame.mixer.init() # Inicia o módulo de som
        pygame.font.init()
        self.tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
        pygame.display.set_caption('Raid Fliperama')
        self.relogio = pygame.time.Clock()
        self.logica = LogicaRaid()
        self.high_scores = carregar_scores()

        # Gera os sons ao iniciar o jogo
        self.som_laser = gerar_som_laser()
        self.som_explosao = gerar_som_explosao()

    def desenhar_jogo(self):
        self.tela.fill(AZUL_RIO)
        jogador_dict = self.logica.jogador
        pontos_jogador = [
            (jogador_dict['x'] + jogador_dict['largura'] / 2, jogador_dict['y']),
            (jogador_dict['x'], jogador_dict['y'] + jogador_dict['altura']),
            (jogador_dict['x'] + jogador_dict['largura'], jogador_dict['y'] + jogador_dict['altura'])
        ]
        pygame.draw.polygon(self.tela, VERDE, pontos_jogador)

        for inimigo in self.logica.inimigos:
            pygame.draw.rect(self.tela, VERMELHO, (inimigo['x'], inimigo['y'], inimigo['largura'], inimigo['altura']))

        for laser in self.logica.lasers_jogador:
            pygame.draw.rect(self.tela, COR_LASER_JOGADOR, (laser['x'], laser['y'], laser['largura'], laser['altura']))
        
        self.desenhar_interface()

    def desenhar_interface(self):
        fonte = pygame.font.SysFont('comicsans', 30, bold=True)
        texto_pontos = fonte.render(f'Pontos: {self.logica.pontuacao}', 1, BRANCO)
        self.tela.blit(texto_pontos, (10, 10))

    def tela_texto(self, texto, tamanho, cor, y_pos, bold=True):
        fonte = pygame.font.SysFont('comicsans', tamanho, bold=bold)
        render_texto = fonte.render(texto, 1, cor)
        self.tela.blit(render_texto, (LARGURA_TELA/2 - render_texto.get_width()/2, y_pos))

    def tela_pausa(self):
        overlay = pygame.Surface((LARGURA_TELA, ALTURA_TELA), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        self.tela.blit(overlay, (0, 0))
        self.tela_texto('PAUSADO', 80, AMARELO, 200)
        self.tela_texto('Pressione P para continuar', 40, BRANCO, 300)
        self.tela_texto('Pressione S para sair da partida', 40, BRANCO, 350)
    
    def tela_inicial(self):
        run = True
        while run:
            self.tela.fill(AMARELO)
            self.tela_texto('RAID FLIPERAMA', 70, PRETO, 150)
            self.tela_texto('Pressione I para iniciar ou S para sair', 40, PRETO, 250)
            y_controles = 350
            self.tela_texto('--- Controles ---', 35, PRETO, y_controles)
            self.tela_texto('Setas Esq/Dir - Mover a Nave', 25, PRETO, y_controles + 50, bold=False)
            self.tela_texto('Espaço - Atirar', 25, PRETO, y_controles + 80, bold=False)
            self.tela_texto('P - Pausar o Jogo', 25, PRETO, y_controles + 110, bold=False)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: run = False; pygame.quit(); sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_i: self.run()
                    if event.key == pygame.K_s: run = False; pygame.quit(); sys.exit()
        
    def tela_game_over(self):
        self.high_scores = adicionar_score(self.iniciais_jogador, self.logica.pontuacao)
        run = True
        while run:
            self.tela.fill(PRETO)
            self.tela_texto('GAME OVER', 80, VERMELHO, 150)
            self.tela_texto(f'Pontuação Final: {self.logica.pontuacao}', 50, BRANCO, 250)
            self.tela_texto('Pressione R para reiniciar ou S para sair', 40, BRANCO, 350)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: pygame.quit(); sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r: self.logica.resetar_jogo(); self.run()
                    if event.key == pygame.K_s: pygame.quit(); sys.exit()

    def tela_inserir_nome(self):
        iniciais = ""
        run = True
        while run:
            self.tela.fill(PRETO)
            self.tela_texto('NOVO RECORDE!', 60, AMARELO, 150)
            self.tela_texto('Digite suas 3 iniciais:', 40, BRANCO, 250)
            self.tela_texto(iniciais.upper(), 70, BRANCO, 320)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: pygame.quit(); sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(iniciais) == 3:
                        self.iniciais_jogador = iniciais.upper(); run = False
                    elif event.key == pygame.K_BACKSPACE: iniciais = iniciais[:-1]
                    elif len(iniciais) < 3 and event.unicode.isalpha(): iniciais += event.unicode

    def run(self):
        rodando = True
        pausado = False
        while rodando:
            self.relogio.tick(VELOCIDADE_JOGO)

            for event in pygame.event.get():
                if event.type == pygame.QUIT: rodando = False; pygame.quit(); sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p: pausado = not pausado
                    if pausado and event.key == pygame.K_s: self.logica.game_over = True; pausado = False
                    if not pausado and event.key == pygame.K_SPACE:
                        evento_som = self.logica.jogador_atira()
                        if evento_som == 'laser': self.som_laser.play()
            
            if not pausado and not self.logica.game_over:
                teclas = pygame.key.get_pressed()
                movimento_x = 0
                if teclas[pygame.K_LEFT]: movimento_x -= VELOCIDADE_JOGADOR
                if teclas[pygame.K_RIGHT]: movimento_x += VELOCIDADE_JOGADOR
                self.logica.mover_jogador(movimento_x)
                
                eventos_som = self.logica.update()
                for som in eventos_som:
                    if som == 'explosao':
                        self.som_explosao.play()

            if self.logica.game_over:
                self.tela_inserir_nome(); self.tela_game_over(); rodando = False
            
            self.desenhar_jogo()
            if pausado: self.tela_pausa()
            pygame.display.update()