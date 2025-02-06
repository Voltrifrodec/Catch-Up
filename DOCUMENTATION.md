# Dokumentácia k aplikácii: Catch Up!

## 1 Vytvorenie nového projektu

### 1.1 Základy

- vytvorenie nového súboru: `__main__.py`
- pridanie *pygame* a *sys* knižnice
- vytvorenie konštánt pre farbu, veľkosti okna, padding/margin, ...
- vytvorenie súboru `scripts/Game.py`, ktorý obsahuje definíciu pre nastavenie obrazovky a samotnej hry
  - vytvorenie funkcií: **initialize**, **update**, **draw**, **quit**
- nastavenie okna, farby, hlavnej game loop, ...
- vytvorenie novej inštancie Game a nastavenie parametrov

### 1.2 Vytvorenie menu a obrazoviek

#### 1.2.1 Vytvorenie triedy Scene
- vytvorenie triedy
- aktualizovanie triedy Game
- pridanie onClickEventListener-ish funkcionality

#### 1.2.2 Vytvorenie scény OnboardingScene
- vytvorenie triedy Text, z *moon-patrol-umb*
- pridanie nadpisu, podnadpisu a spodného textu
- pridanie tlačidla pre spustenie hry (bez funkcionality)
- pridanie pozadia, zmena farby
- pridanie tlačila Exit



## X Bonusy

### X.1 Pridanie hudby a zvukových efektov
- vytvorenie triedy BackroundMusic
- spustenie skladby
- úprava triedy Game
