# Triedy pre nastavenie a spustenie hudby na pozadi
import pygame

# Trieda pre hlavnu hudbu
class BackgroundMusic():
    # V konstruktore priamo nastavim co sa ma prehravat dookola
    def __init__(self):
        # self.music_asset_path = "assets/04-faun-tanz-mit-mir.mp3"
        self.music_asset_path = "assets/tanz-mit-mir-instrumental.mp3"
        self.mixer = pygame.mixer # Redundant
        self.mixer.init() # Redundant
        pass

    # Spustenie hudby
    def play(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.music_asset_path)
        pygame.mixer.music.play(loops=True)

    # Zastavenie hudby
    def stop(self):
        pygame.mixer.music.stop()

# Trieda pre hudbu konca hry (game over)
class GameOverBackgroundMusic():
    # Konstruktor
    def __init__(self):
        self.music_asset_path = "assets/wind-128967.mp3"

    # Spustenie hudby
    def play(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.music_asset_path)
        pygame.mixer.music.play(loops=True)

    # Zastavenie hudby
    def stop(self):
        pygame.mixer.music.stop()
