# Logica da cobrinha

import pygame


class Snake:
    def __init__(self):
        self.cor = (0, 255, 0) # Cor da cobrinha
        self.tamanho = 18 # Tamanho de cada parte do corpo
        self.corpo = [(100, 100), (90, 100), (80, 100)] # Lista de coordenadas
        self.direcao = "DIREITA" # Direção inícial


    def mover(self):
        # Move a cobrinha com base na direção
        cabeca = self.corpo[0]
        if self.direcao == "DIREITA":
            nova_cabeca = (cabeca[0] + self.tamanho, cabeca[1])
        
        elif self.direcao == "ESQUERDA":
            nova_cabeca = (cabeca[0] - self.tamanho, cabeca[1])
        
        elif self.direcao == "CIMA":
            nova_cabeca = (cabeca[0], cabeca[1] - self.tamanho)
        
        elif self.direcao == "BAIXO":
            nova_cabeca = (cabeca[0], cabeca[1] + self.tamanho)
        
        # Coloca a nova cabeça no início da lista
        self.corpo = [nova_cabeca] + self.corpo[:1]

    
    def crescer(self):
        # Adiciona uma nova parte ao corpo
        cauda = self.corpo[-1]
        self.corpo.append(cauda)

    
    def desenhar(self, tela):
        for segmento in self.corpo:
            pygame.draw.rect(tela, self.cor, pygame.Rect(segmento[0], segmento[1], self.tamanho, self.tamanho))
            