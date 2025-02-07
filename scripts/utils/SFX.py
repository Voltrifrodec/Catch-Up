import pygame
import random

class SFX():
    def __init__(self, sound_path = None):
        self.sound_path = sound_path
        self.mixer = pygame.mixer.Sound(file=sound_path)

    def play(self):
        self.mixer.play(self.sound_path)

class sfx_gun(SFX):
    def __init__(self, sound_path="assets/submachine-gun-79846.mp3"):
        super().__init__(sound_path)
        self.mixer = pygame.mixer.Sound(file=sound_path)

    def play(self):
        self.mixer.play()


class sfx_male_scream_1(SFX):
    def __init__(self, sound_path="assets/male-scream-2.mp3"):
        super().__init__(sound_path)
        self.mixer = pygame.mixer.Sound(file=sound_path)

    def play(self):
        self.mixer.play()

class sfx_male_scream_2(SFX):

    def __init__(self, sound_path="assets/male-scream-1.mp3"):
        super().__init__(sound_path)
        self.mixer = pygame.mixer.Sound(file=sound_path)

    def play(self):
        self.mixer.play()

def playRandomMaleScream():
    random_number = random.randint(0, 1)

    if random_number == 0: sfx_male_scream_1().play()
    if random_number == 1: sfx_male_scream_2().play()

def playGameOverSFX():

    for _ in range(10, random.randint(20,30)):
        pygame.mixer.Channel(0).play(pygame.mixer.Sound(file=f'assets/male-scream-{random.randint(1,3)}.mp3'))
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(file=f'assets/male-scream-{random.randint(1,3)}.mp3'))
        pygame.mixer.Channel(2).play(pygame.mixer.Sound(file=f'assets/male-scream-{random.randint(1,3)}.mp3'))
        pygame.mixer.Channel(3).play(pygame.mixer.Sound(file=f'assets/male-scream-{random.randint(1,3)}.mp3'))
