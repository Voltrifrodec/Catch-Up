import pygame

class BackgroundMusic():
    def __init__(self):
        # self.music_asset_path = "assets/04-faun-tanz-mit-mir.mp3"
        self.music_asset_path = "assets/tanz-mit-mir-instrumental.mp3"
        self.mixer = pygame.mixer
        self.mixer.init()
        pass

    def play(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.music_asset_path)
        pygame.mixer.music.play(loops=True)
    
    def stop(self):
        pygame.mixer.music.stop()

class GameOverBackgroundMusic():
    def __init__(self):
        self.music_asset_path = "assets/wind-128967.mp3"

    def play(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.music_asset_path)
        pygame.mixer.music.play(loops=True)

    def stop(self):
        pygame.mixer.music.stop()
