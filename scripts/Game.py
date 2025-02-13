import pygame
import random, math
from scripts.GameObject import GameObject
from scripts.Player import Player
from scripts.Scene import Scene
from scripts.Projectile import Projectile
from scripts.Enemy import Enemy
from scripts.utils.BackgroundMusic import BackgroundMusic, GameOverBackgroundMusic
from scripts.utils.SFX import playRandomMaleScream, playGameOverSFX

# Trieda Game obsahujuca ...
class Game():
    # Konstruktor
    def __init__(self, window_width: int = 800, window_height: int = 600, fps: int = 60) -> None:
        # Zakladne nastavenie: velkost okna, FPS, nastavenie vykreslovania, ...
        self.window_width = window_width
        self.window_height = window_height
        self.fps = fps
        self.display = pygame.display
        self.event = pygame.event
        self.running = True # Ak je True, tak aplikacia je spustena

        # Inicializacia hudby
        self.backgroundImage = pygame.image.load('assets/snowy-platform_800-599.jpg')
        self.backgroundMusic = BackgroundMusic()
        self.backgroundGameOverMusic = GameOverBackgroundMusic()
        self.backgroundMusic.play()

        # Inicializacia objektov hry: hrac, skore,
        self.player = None
        self.score = 0

        self.initialize() # Inicializacia p ygame aplikacie

    # Inicializacia hry
    def initialize(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode((self.window_width, self.window_height))
        self.setCaption('Catch up (v0)')
        self.scene = Scene(self) # Vytvorenie sceny
        self.scene.initialize()

        # Nastavenie objektov hry a skore
        self.score = 0
        self.objects = []
        self.enemies = []
        self.addPlayer()
        self.direction = None
        self.groundSurfacePositionY = 150 # Konstana pre upravu pozicie

    # Vytvorenie novej hry, resetujem hodnoty objektov a hudbu
    def initializeNewGame(self) -> None:
        self.clock = pygame.time.Clock()
        self.scene.changeScene(self.scene.gameOverScene)
        self.score = 0
        self.objects = []
        self.enemies = []
        self.addPlayer()
        self.direction = None
        if self.isInGame(): 
            self.backgroundGameOverMusic.stop()
            self.backgroundMusic.play()

    # Aktualizovanie nazvu okna
    def setCaption(self, caption: str = '') -> None:
        self.display.set_caption(caption)

    # Aktualizovanie hry (obrazovky)
    def update(self) -> None:
        pygame.display.flip()
        self.clock.tick(self.fps) # Ako rychlo

    # Pridanie hraca do hry
    def addPlayer(self) -> None:
        self.addObject(Player(self.window_width//2, self.window_height - 98, pygame.Color("red"), 'assets/shana.png', self.surface, 72, 48))

    # Pridanie objektu. Nastavujem podla typu vstupneho objektu
    # https://github.com/Voltrifrodec/moon-patrol-umb/blob/feature/difficulty-implementation/scripts/Game.py
    def addObject(self, gameObject: GameObject):
        if isinstance(gameObject, Player): self.player = gameObject
        if isinstance(gameObject, Enemy):self.enemies.append(gameObject)
        if isinstance(gameObject, GameObject): self.objects.append(gameObject)

    # Kontrola, ci sa aktualne nachadzame v hre
    def isInGame(self) -> bool:
        return self.scene.currentScene == self.scene.gameScene

    # Posun GameObject objektov
    def moveObjects(self):
        for obj in self.objects:
            # Hrac
            if isinstance(obj, Player) and self.direction is not None:
                self.player.move(self.direction)

            # Nepriatel: Ak je mimo obrazovky, tak hra skoncila
            if (isinstance(obj, Enemy)):
                isOutOfScreen = obj.isOutOfScreen()
                if (isOutOfScreen):
                    obj.resetPosition()
                    self.executeGameOver()
                else:
                    obj.move()

            # Projektily; ak je mimo obrazovky, tak vymaz objekt
            if (isinstance(obj, Projectile)):
                isOutOfScreen = obj.isOutOfScreen()
                if (isOutOfScreen):
                    self.deleteObject(obj)
                else:
                    obj.move()

    # Posun hraca do lavej strany; Viacmenej zbytocne
    def movePlayerToLeft(self):
        self.direction = 'Left'
        self.player.direction = 'Left'
        # print('Moving player to the left')

    # Posun hraca do pravek strany; Viacmenej zbytocne
    def movePlayerToRight(self):
        self.direction = 'Right'
        # print('Moving player to the right')

    # Strielanie
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

    # Deprecated
    def calculateGroundSurfaceY(self):
        return self.surface.get_height() - self.groundSurfacePositionY

    # Vytvorenie/Vykreslenie noveho nepriatela 
    def enemySpawn(self):
        print(f'Creating enemies...')
        enemy = Enemy(position_x=random.randint(0, 800), position_y=24, width=48, height=48, image_path='assets/enemy.png', surface=self.surface, speed=random.randint(1, 3))
        self.addObject(enemy)

    # Pocet nepriatelov aktualne v hre
    def getEnemiesCount(self):
        return len(self.enemies)

    # Pocet projektilov aktualne v hre
    def getProjectileCount(self):
        return len([obj for obj in self.objects if isinstance(obj, Projectile)])

    # Vymazanie objektu
    def deleteObject(self, obj):
        self.objects.remove(obj)
        del obj

    # Kontrola kolizii a prislusne akcie
    def checkCollisionOnAllObjects(self):
        for obj in self.objects:
            # Nepriatelia - ak narazi do hraca, tak hra skoncila
            if isinstance(obj, Enemy):
                if self.player.checkCollision(obj):
                    self.executeGameOver()
            # Projektily - ak projektil trafi nepriatela, tak ho odstrani
            for enemy in self.enemies:
                if (isinstance(obj, Projectile)):
                    projectile = obj
                    if enemy.checkCollisions(projectile):
                        playRandomMaleScream() # zvukove efekty
                        self.deleteObject(enemy)
                        self.enemies.remove(enemy)
                        self.deleteObject(projectile)
                        self.score += math.ceil(1)
                        return

    # Vykreslenie zmien v scene
    def drawScene(self) -> None:
        self.scene.drawScene()

    # Game over 
    def executeGameOver(self) -> None:
        playGameOverSFX()
        self.backgroundMusic.stop()
        self.backgroundGameOverMusic.play()
        self.scene.changeScene(self.scene.gameOverScene)
        self.initializeNewGame()

    # Ukoncenie aplikacie
    def exit(self) -> None:
        self.running = False
