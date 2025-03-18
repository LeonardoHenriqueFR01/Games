# Lógica principal do game

import pygame
import sys
from snake import Snake
from food import Food
from config import LARGURA_GAME, ALTURA_GAME, FPS


# Iniciaiza o pygame
pygame.init()

# Configuração da tela 
tela = pygame.display.set_mode((LARGURA_GAME, ALTURA_GAME))
pygame.display.set_caption("Jogo da cobrinha")


# Função principal do game
def jogo():
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food(LARGURA_GAME, ALTURA_GAME, snake.tamanho)

    while True:
        # Loop de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.quit:
                pygame.quit()
                sys.exit()
        
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and snake.direcao != "DIREITA":
                    snake.direcao = "ESQUERDA"
                
                elif evento.key == pygame.K_RIGHT and snake.direcao != "ESQUERDA":
                    snake.direcao = "DIREITA"
                
                elif evento.key == pygame.K_UP and snake.direcao != "BAIXO":
                    snake.direcao = "CIMA"
                
                elif evento.key == pygame.K_DOWN and snake.direcao != "CIMA":
                    snake.direcao = "BAIXO"
                
        # Atualiza a posição da cobrinha
        snake.mover()

        # Verifica colisões
        if snake.corpo[0] in snake.corpo[1]: # Colisão com o corpo
            return # Fim de jogo
        
        if not 0 <= snake.corpo[0][0] < LARGURA_GAME or not 0 <= snake.corpo[0][1] < ALTURA_GAME:
            return # Colisão com a parede
                    

        # Verifica se a cobrinha comeu a comida
        if snake.corpo[0] == food.posicao:
            snake.crescer()
            food.posicao = food.gerar_posicao() # Nova comida
        
        # Desenha tudo
        tela.fill((0, 0, 0))
        snake.desenhar(tela)
        food.desenhar(tela)

        # Atualiza a tela
        pygame.display.flip()

        # Controla o FPS
        clock.tick(FPS)


if __name__ == "__main__":
    jogo()
