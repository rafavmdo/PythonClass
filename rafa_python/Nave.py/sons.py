# sons.py
import pygame
import numpy as np

# Configurações de áudio
SAMPLE_RATE = 44100  # Taxa de amostragem padrão para áudio de CD
DTYPE = np.int16     # Tipo de dado para as amostras de áudio

def gerar_onda_senoidal(frequencia, duracao_ms):
    """Gera uma onda senoidal simples."""
    num_amostras = int(SAMPLE_RATE * duracao_ms / 1000.0)
    amplitude = 4096  # Controla o volume

    # Gera um array de tempo de 0 até a duração
    t = np.linspace(0., duracao_ms / 1000.0, num_amostras)
    
    # Fórmula da onda senoidal
    data = amplitude * np.sin(2. * np.pi * frequencia * t)
    
    return data.astype(DTYPE)

def gerar_ruido_branco(duracao_ms):
    """Gera um ruído branco (aleatório)."""
    num_amostras = int(SAMPLE_RATE * duracao_ms / 1000.0)
    amplitude = 4096

    # Gera amostras aleatórias entre -amplitude e +amplitude
    data = np.random.uniform(-amplitude, amplitude, num_amostras)
    
    return data.astype(DTYPE)

def gerar_som_laser():
    """Cria o som de um tiro de laser."""
    # Uma nota alta e curta
    onda = gerar_onda_senoidal(frequencia=880.0, duracao_ms=100)
    # Pygame precisa de um array estéreo (2 canais), então duplicamos a onda
    som_stereo = np.repeat(onda.reshape(len(onda), 1), 2, axis=1)
    return pygame.sndarray.make_sound(som_stereo)

def gerar_som_explosao():
    """Cria o som de uma explosão simples."""
    # Ruído branco curto
    onda = gerar_ruido_branco(duracao_ms=300)
    som_stereo = np.repeat(onda.reshape(len(onda), 1), 2, axis=1)
    return pygame.sndarray.make_sound(som_stereo)