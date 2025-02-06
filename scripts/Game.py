import pygame
import random, math
from scripts.GameObject import GameObject
from scripts.Player import Player
from scripts.Scene import Scene
from scripts.Projectile import Projectile
from scripts.utils.BackgroundMusic import BackgroundMusic

# Trieda Game obsahujuca ...
class Game():
    # Konstruktor
    def __init__(self, window_width: int = 800, window_height: int = 600, fps: int = 60) -> None:
        self.window_width = window_width
        self.window_height = window_height
        self.fps = fps
        self.display = pygame.display
        self.event = pygame.event
        self.backgroundImage = pygame.image.load('assets/snowy-platform_800-599.jpg')
        self.backgroundMusic = BackgroundMusic()
        self.backgroundMusic.play()
        self.player = None

        self.initialize() # Inicializacia pygame aplikacie
        self.running = True # Ak je True, tak aplikacia je spustena

    # Inicializacia hry
    def initialize(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode((self.window_width, self.window_height))
        self.setCaption('Catch up (v0)')
        self.scene = Scene(self)
        self.scene.initialize()
        self.score = 0
        self.objects = []
        self.addPlayer()
        self.direction = None

    # Aktualizovanie nazvu okna
    def setCaption(self, caption: str = '') -> None:
        self.display.set_caption(caption)

    # Aktualizovanie hry (obrazovky)
    def update(self) -> None:
        pygame.display.flip()
        self.clock.tick(self.fps) # Ako rychlo

    def addPlayer(self) -> None:
        self.addObject(Player(self.window_width//2, self.window_height - 98, pygame.Color("red"), 'assets/shana.png', self.surface, 72, 48))

    # https://github.com/Voltrifrodec/moon-patrol-umb/blob/feature/difficulty-implementation/scripts/Game.py
    def addObject(self, gameObject: GameObject):
        if isinstance(gameObject, Player): self.player = gameObject
        if isinstance(gameObject, GameObject): self.objects.append(gameObject)
        # self.objects.appent()
        # if isinstance(gameObject, Enemy):self.enemies.append(gameObject)
        # if isinstance(gameObject, GameObject): self.objects.append(gameObject)

    # Posun GameObject objektov
    def moveObjects(self):
        if self.direction is not None:
            self.player.move(self.direction)
        for gameObject in self.objects:
            gameObject.move()

    def movePlayerToLeft(self):
        self.direction = 'Left'
        self.player.direction = 'Left'
        print('Moving player to the left')
        # self.player.moveLeft()

    def movePlayerToRight(self):
        self.direction = 'Right'
        print('Moving player to the right')
        # self.player.moveRight()

    def playerShootProjectile(self):
        projectileObject = self.player.shoot()
        self.addObject(projectileObject)

    # Vykreslenie vsetkych GameObject objektov naraz
    def drawAllObjects(self):
        self.player.draw()
        for gameObject in self.objects:
            print(f'Object: {gameObject}')
            gameObject.draw()

    # Vykreslenie zmien - tu sa vykresluju objekty a zmeny
    def draw(self) -> None:
        self.surface.fill(pygame.Color("black"))
        self.surface.blit(self.backgroundImage, (0, 0))
        self.moveObjects()
        self.drawAllObjects()
        self.checkCollisionOnAllObjects()

    def checkCollisionOnAllObjects(self):
        for obj in self.objects:
            pass
            # Enemies
            # if isinstance(obj, Enemy):
            #     if self.player.checkcollisions(obj):
            #         self.endCurrentGame()
            # Check destroying enemies
            # for enemy in self.enemies:
            #     if (isinstance(obj, Projectile)):
            #         projectile = obj
            #         if enemy.checkcollisions(projectile):
            #             print("\tBoom, he got shot fr ong +1 L ration average Bratislava resident vibes 2004 Techno House Party")
            #             self.deleteObject(enemy)
            #             self.enemies.remove(enemy)
            #             self.deleteObject(projectile)
            #             self.score += math.ceil(1 * self.difficulty.value["scoreMultipler"])
            #             return

    def drawScene(self) -> None:
        self.scene.drawScene()

    # Ukoncenie aplikacie
    def exit(self) -> None:
        self.running = False
