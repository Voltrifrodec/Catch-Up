import pygame

class BackgroundMusic():
    def __init__(self):
        self.music_asset_path = "assets/04-faun-tanz-mit-mir.mp3"
        self.mixer = pygame.mixer
        self.mixer.init()
        pass

    def play(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.music_asset_path)
        pygame.mixer.music.play(loops=1)
