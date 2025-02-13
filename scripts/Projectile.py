# Trieda pre projektil
# Reference: https://github.com/Voltrifrodec/moon-patrol-umb/blob/feature/difficulty-implementation/scripts/Projectile.py

import pygame
from scripts.GameObject import GameObject
from scripts.Direction import Direction

# Hlavna trieda (dedi z GameObject)
class Projectile(GameObject):
    # Konstruktor
    def __init__(self, position_x: int = 0, position_y: int = 98, color: pygame.Color = pygame.Color("black"), image_path: str = None, surface: pygame.Surface = None, width: int = 8, height: int = 8, direction = Direction.TOP, projectileSpeed= 8):
        super().__init__(position_x, position_y, color, image_path, surface, width, height)
        
        # Doplname rychlost projektilu, jeho tvar a smer
        self.projectileSpeed = projectileSpeed
        self.rect = pygame.Rect(self.position_x, self.position_y, self.width, self.height)
        self.direction = direction

    # Posun projektilu podla urceneho smeru
    # V buducnosti vdaka tomuto vieme nastavit, aby napr. nepriatelia vedeli strielat na hraca
    def move(self):
        if(self.direction == Direction.TOP):
            self.rect.y += Direction.TOP.value * self.projectileSpeed * 100
        if(self.direction == Direction.BOTTOM):
            self.rect.y += Direction.BOTTOM.value * self.projectileSpeed * 100
        else:
            pass

    # Kontrola, ci je projektil este na obrazovke
    def isOutOfScreen(self) -> bool:
        if self.rect.y < 0 or self.rect.y > 600:
            return True

        return False

    # Vykreslenie projektilu na suradnice
    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)
