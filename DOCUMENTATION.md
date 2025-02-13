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


## 2 Práca na hre

### 2.1 Vytvorenie univerzálnej triedy GameObject
- vytvorenie novej triedy GameObject

### 2.2 Vytvorenie hráča
- vytvorenie obrázku pre hráča
- pridanie osy pohybu
- pridanie podpory klávesových skratiek
- pridanie pohybu a prepočtu súradníc pre pohyb

### 2.3 Pridanie strelania
- vytvorenie triedy Projectile
- nastavenie streľby v hlavnom cykle (klávesová skratka SPACE)

### 2.4 Pridanie nepriateľov
- vytvorenie triedy Enemy
- pridanie logiky pre pohyb
- pridanie kolízií s hráčom a guľkou
- pridanie počítania skóre

## 3 Vylepšovanie hry

### 3.1 Pridanie 'Game Over' scény

<!-- ## 3 Logika hr -->

## X Bonusy

### X.1 Pridanie hudby a zvukových efektov
- vytvorenie triedy BackroundMusic
- spustenie skladby
- úprava triedy Game

### X.2 Pridanie zvukových efektov pre akcie
- vytvorenie novej triedy SFX
- vytvorenie triedy sfx_gun, ktorá prehráva zvuk streľby zo zbrane