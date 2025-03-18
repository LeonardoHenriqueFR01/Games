# Lógica de comida que a cobrinha vai comer

import pygame
from random import randint


class Food:
    def __init__(self, largura, altura, tamanho):
        self.largura = largura
        self.altura = altura
        self.tamanho = tamanho
        self.cor = (255, 0, 0) # Cor da comida
        self.posicao = self.gerar_posicao()

    
    def gerar_posicao(self):
        # Gera uma posição aleatória para a comida
        x = randint(0, (self.largura - self.tamanho) // self.tamanho) * self.tamanho
        y = randint(0, (self.altura - self.tamanho) // self.tamanho) * self.tamanho
        return (x, y)
    

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, pygame.Rect(self.posicao[0], self.posicao[1], self.tamanho, self.tamanho))
        