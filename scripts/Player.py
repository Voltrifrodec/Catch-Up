import pygame

from scripts.GameObject import GameObject
# from scripts.Game import WINDOW_WIDTH # 800

class Player(GameObject):
    def __init__(self, position_x = 0, position_y = 0, color = pygame.Color("red"), image_path = None, surface = None, width = 96, height = 48):
        super().__init__(position_x, position_y, color, image_path, surface, width, height)
        self.startingPosition = position_x, position_y
        self.movementSpeed = 0.145
        self.shootingSpeed = 0.065
        self.projectileSpeed = 0.08
        self.position_x_limit = 800  # Redundant?

    def move(self, direction=None):
        print(self.position_x, self.position_y)

        if direction is None:
            return
        if direction == 'Left':
            self.moveLeft()
        elif direction == 'Right':
            self.moveRight()

        # if (self.position_x <= 0):
        #     print("Trafil si lavu stenu/Si za lavou stenou")
        # if (self.position_x >= 800):
        #     print("Trafil si pravu stenu/Si za pravou stenou")

    def moveLeft(self):
        print(f"Going left: {self.position_x}")
        if (self.position_x + self.width) <= self.width:
            self.position_x = 0
            print("Trafil si lavu stenu/Si za lavou stenou")
            return
        else:
            self.position_x -= 100 * self.movementSpeed

    def moveRight(self):
        print(f'Going right: {self.position_x}')
        if (self.position_x + self.width >= 800):
            self.position_x = 800 - self.width
            print("Trafil si pravu stenu/Si za pravou stenou")
        else:
            self.position_x += 100 * self.movementSpeed

    def draw(self):
        print(f'Image: {self.image}')
        if self.image is not None:
            self.rect = self.image.get_rect(x=self.position_x, y=self.position_y)
            self.surface.blit(self.image, self.rect)

    def checkCollision(self, obj: GameObject):
        return self.rect.colliderect(obj.rect)
