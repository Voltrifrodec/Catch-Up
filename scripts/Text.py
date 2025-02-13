# Trieda pre nastavenie a vykreslovanie textu v hre
# Reference: https://github.com/Voltrifrodec/moon-patrol-umb/blob/feature/difficulty-implementation/scripts/Text.py
import pygame

# Premenne pre farby
WHITE = pygame.Color("white")
ICY_BLUE = pygame.Color((103, 222, 205))
BLACK = pygame.Color("black")

# Velkosti jednotlivych typov textu
FONT_SIZE_BUTTON = 40
FONT_SIZE_TITLE = 80
FONT_SIZE_TEXT = 14
FONT_SIZE_FOOTER = 10

# Hlavna trieda
class Text:
    # Konstruktor
    def __init__(self, text: str, fontSizePixel: int, position: tuple[int, int] = (0, 0), font: str = "assets/unispace bd.ttf",
        antialias: bool = True, textColor=ICY_BLUE
    ) -> None:
        self.text = text
        self.fontSizePixel = fontSizePixel
        self.position = position
        self.font = self.validateFont(font)
        self.rendered = self.font.render(self.text, antialias, textColor)
        self.rectangle = self.rendered.get_rect(topleft=(self.position)) # Ukladanie textu

        # Urcovanie velkosti textu
        self.textSize = self.font.size(self.text)
        self.width = self.textSize[0]
        self.height = self.textSize[1]

    # Zmena textu
    def changeTo(self, text):
        self.text = text

    # Zmena pozicie
    def changePosition(self, position):
        self.position = position
        self.rectangle = self.rendered.get_rect(topleft=(self.position))

    # Dolezita kontrola kolizie -- vyuzivanie pre tlacidla v menu (onclick)
    def doesCollide(self, x: int, y: int):
        return self.rectangle.collidepoint(x, y)

    # Kontrola, ci je font dostupny
    # (mal som problemy pretoze mi nechcelo nacitavat styly, toto to kontroluje)
    def validateFont(self, font: str) -> pygame.font.Font:
        try:
            return pygame.font.Font(font, self.fontSizePixel)
        except FileNotFoundError as e:
            defaultFontPath = "assets/unispace bd.ttf"
            print(f"{e}")
            print(f"Using the default font: {defaultFontPath}")
            return pygame.font.Font(defaultFontPath, self.fontSizePixel)
