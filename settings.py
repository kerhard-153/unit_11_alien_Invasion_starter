from pathlib import Path

class Settings:

    def __init__(self):
        self.name: str = "Alien Invasion"
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / 'unit_11_alien_Invasion_game' / 'Assets' / 'images' / 'galaxy_.png'

        self.ship_file = Path.cwd() / 'unit_11_alien_Invasion_game'/ 'Assets' / 'images' / 'spaceship.png'
        self.ship_w = 64
        self.ship_h = 64
        self.ship_speed = 5