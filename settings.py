from pathlib import Path

class Settings:

    def __init__(self):

        """
        Initializes game settings

        Attributes
        ----------

        name (str)
            name of the game (caption)
        screen_w (int)
            width of screen
        screen_h (int)
            height of screen
        FPS (int)
            frames per second, used by Clock()
        bg_file (file)
            accesses background image file
        ship_file (file)
            accesses ship image file
        ship_w (int)
            sets the ship width
        ship_h (int)
            sets the ship height
        ship_speed (int)
            sets ship speed (x-coordinates)

        """
        self.name: str = "Alien Invasion"
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / 'unit_11_alien_Invasion_game' / 'Assets' / 'images' / 'galaxy_.png'

        self.ship_file = Path.cwd() / 'unit_11_alien_Invasion_game'/ 'Assets' / 'images' / 'spaceship.png'
        self.ship_w = 64
        self.ship_h = 64
        self.ship_speed = 5