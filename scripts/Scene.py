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
        self.changeScene(self.mainMenuScene)

    def changeScene(self, scene: 'Scene'): # v '' pretoze volame rovnaky typ v akom je definovana funkcia
        self.currentScene = scene

    def drawScene(self) -> None:
        self.currentScene.drawScene()


class OnboardingScene(Scene) :
    # Konstruktor
    def __init__(self, game: Game):
        super().__init__(game)
        self.name = 'Catch Up (v0)'
        self.initializeSceneObjects()

    def initializeSceneObjects(self) -> None:

        # Nadpis, Podnadpis
        self.gameTitleText = Text('Catch Up!', FONT_SIZE_TITLE)
        self.gameTitleText.changePosition((self.game.window_width//2 - self.gameTitleText.width//2, self.game.window_height//6 - self.gameTitleText.fontSizePixel//2))
        self.gameSubtitleText = Text('Family friendy shooter', FONT_SIZE_TEXT)
        self.gameSubtitleText.changePosition((self.game.window_width//2 - self.gameSubtitleText.width//2, self.game.window_height//3 - self.gameSubtitleText.fontSizePixel//2))

        # Vytvorenie hlavneho menu
        self.startGameText = Text('PLAY', FONT_SIZE_BUTTON)
        self.startGameText.changePosition((self.game.window_width//2 - self.startGameText.width//2, self.game.window_height//2 - self.startGameText.fontSizePixel//2))

        # Copyright claim
        self.upperFooterText = Text("© 2025 Jakub V. Frodec", FONT_SIZE_FOOTER)
        self.upperFooterText.changePosition((self.game.window_width//2 - self.upperFooterText.width//2, self.game.window_height - self.upperFooterText.fontSizePixel*6))
        self.lowerFooterText = Text("Fakulta prírodných vied univerzity Mateja Bela v Banskej Bystrici", FONT_SIZE_FOOTER)
        self.lowerFooterText.changePosition((self.game.window_width//2 - self.lowerFooterText.width//2, self.game.window_height - self.lowerFooterText.fontSizePixel*4))

    def drawScene(self) -> None:
        self.game.surface.fill(BLACK)
        self.game.surface.blit(self.startGameText.rendered, self.startGameText.position)
        self.game.surface.blit(self.gameTitleText.rendered, self.gameTitleText.position)
        self.game.surface.blit(self.gameSubtitleText.rendered, self.gameSubtitleText.position)
        self.game.surface.blit(self.upperFooterText.rendered, self.upperFooterText.position)
        self.game.surface.blit(self.lowerFooterText.rendered, self.lowerFooterText.position)
