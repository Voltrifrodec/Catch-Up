import pygame

from scripts.Game import Game
from scripts.Scene import GameScene

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

        if pygame.mouse.get_pressed(3)[0]:
            game.scene.currentScene.update(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

        if isinstance(game.scene.currentScene, GameScene):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                game.movePlayerToLeft()
            if keys[pygame.K_d]:
                game.movePlayerToRight()
            if event.type == pygame.KEYUP:
                game.direction = None

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game.playerShootProjectile()


        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_a:
        #         game.movePlayerToLeft()

        #     if event.key == pygame.K_d:
        #         game.movePlayerToRight()

        if event.type == pygame.QUIT:
            game.exit()
            break

    game.drawScene()
    game.update()
