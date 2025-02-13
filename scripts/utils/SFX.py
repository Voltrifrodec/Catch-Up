import pygame
import random

# Trieda pre specialne efekty (sound effects)
class SFX():
    # Konstruktor
    def __init__(self, sound_path = None):
        self.sound_path = sound_path
        self.mixer = pygame.mixer.Sound(file=sound_path)

    # Spustenie zvuku
    def play(self):
        self.mixer.play(self.sound_path)

# Zvuk strielania
class sfx_gun(SFX):
    # Konstruktor
    def __init__(self, sound_path="assets/submachine-gun-79846.mp3"):
        super().__init__(sound_path)
        self.mixer = pygame.mixer.Sound(file=sound_path)

    # Spustenie zvuku
    def play(self):
        self.mixer.play()


# Zvuk vykriku pre nepriatela (moznost 1)
class sfx_male_scream_1(SFX):
    # Konstruktor
    def __init__(self, sound_path="assets/male-scream-2.mp3"):
        super().__init__(sound_path)
        self.mixer = pygame.mixer.Sound(file=sound_path)

    # Spustenie zvuku
    def play(self):
        self.mixer.play()


# Zvuk vykriku pre nepriatela (moznost 2)
class sfx_male_scream_2(SFX):
    # Konstruktor
    def __init__(self, sound_path="assets/male-scream-1.mp3"):
        super().__init__(sound_path)
        self.mixer = pygame.mixer.Sound(file=sound_path)

    # Spustenie zvuku
    def play(self):
        self.mixer.play()

# Spustenie nahodneho zvuku pre nepriatela
def playRandomMaleScream():
    random_number = random.randint(0, 1)

    if random_number == 0: sfx_male_scream_1().play()
    if random_number == 1: sfx_male_scream_2().play()

# Zvuk pre koniec hry (musi byt neprijemny, pre motivaciu :-))
def playGameOverSFX():
    for _ in range(10, random.randint(20,30)):
        pygame.mixer.Channel(0).play(pygame.mixer.Sound(file=f'assets/male-scream-{random.randint(1,3)}.mp3'))
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(file=f'assets/male-scream-{random.randint(1,3)}.mp3'))
        pygame.mixer.Channel(2).play(pygame.mixer.Sound(file=f'assets/male-scream-{random.randint(1,3)}.mp3'))
        pygame.mixer.Channel(3).play(pygame.mixer.Sound(file=f'assets/male-scream-{random.randint(1,3)}.mp3'))
