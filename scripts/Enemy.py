import pygame
from scripts.GameObject import GameObject


class Enemy(GameObject):
    def __init__(self, position_x: int = 0, position_y: int = 0, color: pygame.Color = pygame.Color("red"), image_path: str = None, surface: pygame.Surface = None, width: int = 48, height: int = 24, speed=1):
        super().__init__(position_x, position_y, color, image_path, surface, width, height)
        self.speed = speed
        self.rect = self.image.get_rect(x=self.position_x, y=self.position_y)
        self.default_position_x = position_x
        self.default_position_y = position_y

    def move(self):
        self.position_y += self.speed

    def draw(self):
        self.rect = self.image.get_rect(x=self.position_x, y=self.position_y)
        self.surface.blit(self.image, self.rect)

    def resetPosition(self):
        self.position_x = self.default_position_x
        self.position_y = self.default_position_y

    def isOutOfScreen(self):
        return self.position_y + self.height > 600

    def checkCollisions(self, object: GameObject):
        return self.rect.colliderect(object.rect)
