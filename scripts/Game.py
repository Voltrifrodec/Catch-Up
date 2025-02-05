import pygame
import random

# Trieda Game obsahujuca ...
class Game():
    # Konstruktor
    def __init__(self, window_width: int = 800, window_height: int = 600, fps: int = 60) -> None:
        self.window_width = window_width
        self.window_height = window_height
        self.fps = fps
        self.display = pygame.display
        self.event = pygame.event

        self.initialize() # Inicializacia pygame aplikacie
        self.running = True # Ak je True, tak aplikacia je spustena

    # Inicializacia hry
    def initialize(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode((self.window_width, self.window_height))
        self.setCaption('Catch up (v0)')
        self.score = 0

    # Aktualizovanie nazvu okna
    def setCaption(self, caption: str = '') -> None:
        self.display.set_caption(caption)

    # Aktualizovanie hry (obrazovky)
    def update(self) -> None:
        pygame.display.flip()
        self.clock.tick(self.fps) # Ako rychlo

    # Vykreslenie zmien - tu sa vykresluju objekty a zmeny
    def draw(self) -> None:
        self.surface.fill(pygame.Color('BLACK'))

    # Ukoncenie aplikacie
    def exit(self) -> None:
        self.running = False