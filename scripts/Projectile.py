import pygame
from scripts.GameObject import GameObject
from scripts.Direction import Direction

class Projectile(GameObject):
    def __init__(self, position_x: int = 0, position_y: int = 98, color: pygame.Color = pygame.Color("black"), image_path: str = None, surface: pygame.Surface = None, width: int = 4, height: int = 4, direction = Direction.TOP, projectileSpeed= 8):
        super().__init__(position_x, position_y, color, image_path, surface, width, height)
        self.projectileSpeed = projectileSpeed
        self.rect = pygame.Rect(self.position_x, self.position_y, self.width, self.height)
        self.direction = direction

    def move(self):
        if(self.direction == Direction.TOP):
            self.rect.y += Direction.TOP.value * self.projectileSpeed * 100
        if(self.direction == Direction.BOTTOM):
            self.rect.y += Direction.BOTTOM.value * self.projectileSpeed * 100
        else:
            pass

    # https://github.com/Voltrifrodec/moon-patrol-umb/blob/feature/difficulty-implementation/scripts/Projectile.py
    def isOutOfScreen(self) -> bool:
        if self.rect.y < 0 or self.rect.y > 600:
            return True

        return False

    def draw(self):
        print(self.rect.y)
        pygame.draw.rect(self.surface, self.color, self.rect)
