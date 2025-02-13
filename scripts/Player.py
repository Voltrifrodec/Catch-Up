# Trieda pre hraca
import pygame

from scripts.GameObject import GameObject
from scripts.Projectile import Projectile
from scripts.Direction import Direction
from scripts.utils.SFX import sfx_gun

# Hlavna trieda
class Player(GameObject):

    # Konstruktor
    def __init__(self, position_x = 0, position_y = 0, color = pygame.Color("red"), image_path = None, surface = None, width = 96, height = 48):
        super().__init__(position_x, position_y, color, image_path, surface, width, height)

        # Doplname startovaciu poziciu, rychlost pohybu a strielaniia, limit pre posuvanie
        self.startingPosition = position_x, position_y
        self.movementSpeed = 0.145
        self.shootingSpeed = 0.0265
        self.projectileSpeed = 0.08
        self.position_x_limit = 800  # Redundant?

    # Posun pre hraca (podla smeru)
    def move(self, direction=None):
        if direction is None:
            return
        if direction == 'Left':
            self.moveLeft()
        elif direction == 'Right':
            self.moveRight()

    # Posun dolava
    def moveLeft(self):
        # Ak hrac je na zaciatku okna, tak sa nemoze posunut viacej dolava
        if (self.position_x + self.width) <= self.width:
            self.position_x = 0
            return
        else:
            self.position_x -= 100 * self.movementSpeed

    # Posun doprava
    def moveRight(self):
        # Ak hrac je na zaciatku okna, tak sa nemoze posunut viacej dolava
        if (self.position_x + self.width >= 800):
            self.position_x = 800 - self.width
        else:
            self.position_x += 100 * self.movementSpeed

    # Vykreslenie hraca (spolu s 2D texturou)
    def draw(self):
        if self.image is not None:
            self.rect = self.image.get_rect(x=self.position_x, y=self.position_y)
            self.surface.blit(self.image, self.rect)

    # Kontrola kolizie
    def checkCollision(self, obj: GameObject):
        return self.rect.colliderect(obj.rect)

    # Funkcionalita pre strielanie -- tam, kde sme stlacili SPACE sa vytvori projektil a prehra zvuk strielania
    def shoot(self):
        [projectile_x, projectile_y] = self.position_x + self.width//2 + 5, self.position_y + (self.height //2)
        sfx_gun().play()
        return Projectile(projectile_x, projectile_y, surface=self.surface, projectileSpeed=self.projectileSpeed, direction=Direction.TOP)
