import pygame
from scripts.GameObject import GameObject

# Hlavna trieda (dedi z GameObject)
class Enemy(GameObject):
    # Konstruktor
    def __init__(self, position_x: int = 0, position_y: int = 0, color: pygame.Color = pygame.Color("red"), image_path: str = None, surface: pygame.Surface = None, width: int = 48, height: int = 24, speed=1):
        super().__init__(position_x, position_y, color, image_path, surface, width, height)
        
        # Nastavujeme doplnujuce parametre: rychlost nepriatela, default pozicia
        self.speed = speed
        self.rect = self.image.get_rect(x=self.position_x, y=self.position_y)
        self.default_position_x = position_x
        self.default_position_y = position_y

    # Posun nepriatela (iba zhora nadol)
    def move(self):
        self.position_y += self.speed

    # Vykreslenie nepriatela a nastavenie 2D textury
    def draw(self):
        self.rect = self.image.get_rect(x=self.position_x, y=self.position_y)
        self.surface.blit(self.image, self.rect)

    # Restart pozicie -- tocime toho isteho nepriatela
    # Viacmenej redundantne
    def resetPosition(self):
        self.position_x = self.default_position_x
        self.position_y = self.default_position_y

    # Kontrola, ci je nepriatel mimo obrazovky
    def isOutOfScreen(self):
        return self.position_y + self.height > 600

    # Kontrola kolizii
    def checkCollisions(self, object: GameObject):
        return self.rect.colliderect(object.rect)
