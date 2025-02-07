import pygame
from scripts import Game
from scripts.Text import Text
from scripts.Text import (
    FONT_SIZE_BUTTON,
    FONT_SIZE_TITLE,
    FONT_SIZE_TEXT,
    FONT_SIZE_FOOTER,
)

BLACK = pygame.Color("black")

class Scene():
    # Konstruktor
    def __init__(self, game: Game):
        self.currentScene: Scene = None
        self.game: Game = game

    def initialize(self) -> None:
        self.mainMenuScene = OnboardingScene(self.game)
        self.gameScene = GameScene(self.game)
        self.gameOverScene = GameOverScene(self.game)
        self.changeScene(self.mainMenuScene)

    def changeScene(self, scene: 'Scene'): # v '' pretoze volame rovnaky typ v akom je definovana funkcia
        self.currentScene = scene

    def drawScene(self) -> None:
        self.currentScene.drawScene()

    def update(self, x:int, y:int) -> None:
        pass


class OnboardingScene(Scene) :
    # Konstruktor
    def __init__(self, game: Game):
        super().__init__(game)
        self.name = 'Catch Up (v0)'
        self.initializeSceneObjects()
        self.game.backgroundGameOverMusic.stop()
        self.game.backgroundMusic.play()

    def initializeSceneObjects(self) -> None:

        # Nastavenie pozadia
        self.backgroundImage = pygame.image.load('assets/darker-snowy-country_800-600.jpg')

        # Nadpis, Podnadpis
        self.gameTitleText = Text('Catch Up!', FONT_SIZE_TITLE)
        self.gameTitleText.changePosition((self.game.window_width//2 - self.gameTitleText.width//2, self.game.window_height//6 - self.gameTitleText.fontSizePixel//2))
        self.gameSubtitleText = Text(
            "Family friendy shooter", FONT_SIZE_TEXT)
        self.gameSubtitleText.changePosition((self.game.window_width//2 - self.gameSubtitleText.width//2, self.game.window_height//3 - self.gameSubtitleText.fontSizePixel//2))

        # Vytvorenie hlavneho menu
        self.startGameText = Text('PLAY', FONT_SIZE_BUTTON)
        self.startGameText.changePosition((self.game.window_width//2 - self.startGameText.width//2, self.game.window_height//2 - self.startGameText.fontSizePixel//2))
        self.exitGameText = Text('EXIT', FONT_SIZE_BUTTON, textColor=pygame.Color("red"))
        self.exitGameText.changePosition((self.game.window_width//2 - self.exitGameText.width//2, self.game.window_height//1.5 - self.exitGameText.fontSizePixel//2))

        # Copyright claim
        self.upperFooterText = Text("© 2025 Jakub V. Frodec", FONT_SIZE_FOOTER)
        self.upperFooterText.changePosition((self.game.window_width//2 - self.upperFooterText.width//2, self.game.window_height - self.upperFooterText.fontSizePixel*6))
        self.lowerFooterText = Text("Fakulta prírodných vied univerzity Mateja Bela v Banskej Bystrici", FONT_SIZE_FOOTER)
        self.lowerFooterText.changePosition((self.game.window_width//2 - self.lowerFooterText.width//2, self.game.window_height - self.lowerFooterText.fontSizePixel*4))

    def drawScene(self) -> None:
        self.game.surface.fill(BLACK)
        self.game.surface.blit(self.backgroundImage, (0, 0))
        self.game.surface.blit(self.startGameText.rendered, self.startGameText.position)
        self.game.surface.blit(self.exitGameText.rendered, self.exitGameText.position)
        self.game.surface.blit(self.gameTitleText.rendered, self.gameTitleText.position)
        self.game.surface.blit(self.gameSubtitleText.rendered, self.gameSubtitleText.position)
        self.game.surface.blit(self.upperFooterText.rendered, self.upperFooterText.position)
        self.game.surface.blit(self.lowerFooterText.rendered, self.lowerFooterText.position)

    def update(self, x: int, y: int) -> None:
        if self.startGameText.doesCollide(x, y):
            self.game.scene.changeScene(self.game.scene.gameScene)
        if self.exitGameText.doesCollide(x, y):
            self.game.exit()

class GameScene(Scene):
    def __init__(self, game: Game):
        super().__init__(game)
        self.name = 'Game in progress'
        self.game = game
        self.initializeSceneObjects()

    def initializeSceneObjects(self) -> None:
        self.textScore = Text(f'SCORE {self.game.score:2}', FONT_SIZE_TEXT)
        pass

    def drawScene(self) -> None:
        self.game.draw()
        self.textScore = Text(f'SCORE {self.game.score:2}', FONT_SIZE_TEXT)
        self.game.surface.blit(self.textScore.rendered, self.textScore.position)
        self.name = f'Game in progress (Score: {self.game.score:2})'

    def update(self, x: int, y: int) -> None:
        pass


class GameOverScene(Scene):
    # Konstruktor
    def __init__(self, game: Game):
        super().__init__(game)
        self.name = "GAME OVER"
        self.initializeSceneObjects()
        self.mainMenuScene = OnboardingScene(self.game)

    def initializeSceneObjects(self) -> None:

        self.sceneTitleText = Text('GAME OVER', FONT_SIZE_TITLE, textColor=pygame.Color("red"))
        self.sceneTitleText.changePosition((self.game.window_width//2 - self.sceneTitleText.width//2, self.game.window_height//6 - self.sceneTitleText.fontSizePixel//2))
        

        self.textScore = Text(f"SCORE {self.game.score:2}", FONT_SIZE_TEXT)
        self.textScore.changePosition((self.game.window_width//2 - self.textScore.width//2, self.game.window_height - self.textScore.fontSizePixel*6))

        self.mainMenuText = Text('MAIN MENU', FONT_SIZE_BUTTON)
        self.mainMenuText.changePosition((self.game.window_width//2 - self.mainMenuText.width//2, self.game.window_height - self.mainMenuText.fontSizePixel*4))

    def drawScene(self) -> None:
        self.game.draw()
        self.game.surface.fill(BLACK)
        self.game.surface.blit(self.textScore.rendered, self.textScore.position)
        self.game.surface.blit(self.mainMenuText.rendered, self.mainMenuText.position)
        self.game.surface.blit(self.sceneTitleText.rendered, self.sceneTitleText.position)
        self.name = f"Game Over! (Score: {self.game.score:2})"

    def update(self, x: int, y: int) -> None:
        if self.mainMenuText.doesCollide(x, y):
            self.mainMenuScene.initialize()
            self.game.scene.changeScene(self.mainMenuScene)
