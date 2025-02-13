# Tried pre objekty v hre
# Reference: https://github.com/Voltrifrodec/moon-patrol-umb/blob/feature/difficulty-implementation/scripts/GameObject.py
import pygame

# Hlavna tried
class GameObject:
    # Konstruktor
    def __init__(self, position_x: int = 0, position_y: int = 0, color: pygame.Color = pygame.Color("red"), image_path: str = None, surface: pygame.Surface = None, width: int = 48, height: int = 24,
    ) -> None:
        self.position_x = position_x
        self.position_y = position_y
        self.color = color
        self.image_path = image_path
        self.image = None
        self.surface = surface

        self.width = width
        self.height = height

        # Viacmenej redundantna podmienkova cast -- nastavujeme farbu objektu ak nie je uvedena 2D textura
        if color is None and image_path is None:
            raise ValueError("One of color or image_path must not be None!")
        if color is not None:
            self.color = pygame.color.Color(color)
        if image_path is not None:
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
            self.rect = self.image.get_rect(x=position_x, y=position_y)
            self.imageWidth = self.image.get_width()
            self.imageHeight = self.image.get_height()

    # Vykreslenie objektu
    def draw(self):
        if self.image is not None:
            self.rect = self.image.get_rect(x=self.position_x, y=self.position_y)
            self.surface.blit(self.image, self.rect)

    # Kontrola kolizii
    def checkcollision(self, x: int, y: int):
        return self.position_x == x or self.position_y == y
