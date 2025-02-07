import pygame
from scripts.GameObject import GameObject

class Booster(GameObject):
    def __init__(self, position_x = 0, position_y = 0, color = ..., image_path = None, surface = None, width = 12, height = 12):
        super().__init__(position_x, position_y, color, image_path, surface, width, height)