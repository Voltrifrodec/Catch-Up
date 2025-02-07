import pygame
import random
from scripts.Game import Game
from scripts.Scene import GameScene
from scripts.utils.SFX import sfx_gun

# Konstanty
## Farby
WHITE = pygame.Color('white')
BLACK = pygame.Color('black')
WINDOW_WIDTH = 800 # TODO: mozno spojit do jedneho
WINDOW_HEIGHT = 600
FPS = 60

# Vytvorenie novej instancie triedy Game
game = Game(window_width = WINDOW_WIDTH, window_height = WINDOW_HEIGHT, fps = FPS)
gun_sound = sfx_gun()

previous_time = pygame.time.get_ticks()
previous_time_enemies = pygame.time.get_ticks()
previous_shooting_time = pygame.time.get_ticks()
while game.running:
    for event in game.event.get():

        if pygame.mouse.get_pressed(3)[0]:
            game.scene.currentScene.update(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        
        if game.isInGame():
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
                    if game.getProjectileCount() <= 10:
                        current_shootin_time = pygame.time.get_ticks()
                        if current_shootin_time - previous_shooting_time > 400:
                            previous_shooting_time = current_shootin_time
                            game.playerShootProjectile()

            if game.getEnemiesCount() <= 5:
                current_time = pygame.time.get_ticks()
                print("Current enemies: {}".format(game.getEnemiesCount()))
                if current_time - previous_time_enemies > random.randint(500,1000):
                    previous_time_enemies = current_time
                    game.enemySpawn()

        if event.type == pygame.QUIT:
            game.exit()
            break

    game.drawScene()
    game.update()
