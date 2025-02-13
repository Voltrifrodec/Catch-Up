import pygame
import random
from scripts.Game import Game
from scripts.Scene import GameScene

# Konstanty pre farby, velkost okna a FPS
WHITE = pygame.Color('white')
BLACK = pygame.Color('black')
WINDOW_WIDTH = 800 # TODO: mozno spojit do jedneho
WINDOW_HEIGHT = 600
FPS = 60

# Vytvorenie novej instancie triedy Game
game = Game(window_width = WINDOW_WIDTH, window_height = WINDOW_HEIGHT, fps = FPS)

# Nastavenie premennych pre hlavny game loop
previous_time = pygame.time.get_ticks()
previous_time_enemies = pygame.time.get_ticks()
previous_shooting_time = pygame.time.get_ticks()

# Hlavny game loop
while game.running:
    # Event listener
    for event in game.event.get():

        # Redundantne: listener pre stacenie tlacidla mysi
        if pygame.mouse.get_pressed(3)[0]:
            game.scene.currentScene.update(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        
        # Kontrola, ci sme v hre a co ma nastat    
        if game.isInGame():

            # Pohyb hraca v pripade, ze je spustena hra
            if isinstance(game.scene.currentScene, GameScene):
                keys = pygame.key.get_pressed()
                if keys[pygame.K_a]:
                    game.movePlayerToLeft()
                if keys[pygame.K_d]:
                    game.movePlayerToRight()
                if event.type == pygame.KEYUP:
                    game.direction = None

            # Strelanie hraca, obmedzene maximalne na 10 projektilov na obrazovke
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if game.getProjectileCount() <= 10:
                        current_shootin_time = pygame.time.get_ticks()
                        # Delay pre strelanie, obmedzeny na 400ms
                        if current_shootin_time - previous_shooting_time > 400:
                            previous_shooting_time = current_shootin_time
                            game.playerShootProjectile()

            # Generovanie nepriatelov (maximalny pocet: 5 sucasne na obrazovke)
            # Nepriatelia sa generuju nahodne v intervale <500;1000>ms
            if game.getEnemiesCount() <= 5:
                current_time = pygame.time.get_ticks()
                # print("Current enemies: {}".format(game.getEnemiesCount()))
                if current_time - previous_time_enemies > random.randint(500,1000):
                    previous_time_enemies = current_time
                    game.enemySpawn()

        # Ukoncenie hry
        if event.type == pygame.QUIT:
            game.exit()
            break

    # Vykreslenie sceny a aktualizovanie hry
    game.drawScene()
    game.update()
