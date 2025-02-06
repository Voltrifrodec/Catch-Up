import pygame

from scripts.Game import Game

# Konstanty
## Farby
WHITE = pygame.Color('white')
BLACK = pygame.Color('black')
WINDOW_WIDTH = 800 # TODO: mozno spojit do jedneho
WINDOW_HEIGHT = 600
FPS = 60

# Vytvorenie novej instancie triedy Game
game = Game(window_width = WINDOW_WIDTH, window_height = WINDOW_HEIGHT, fps = FPS)

while game.running:
    for event in game.event.get():

        if event.type == pygame.QUIT:
            game.exit()
            break

    game.drawScene()
    game.update()
