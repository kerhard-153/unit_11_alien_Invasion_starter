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
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'space.png'

        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'spaceship.png'
        self.ship_w = 64
        self.ship_h = 64
        self.ship_speed = 5

        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'green_laser2.png'
        self.bullet_file_pink = Path.cwd() / 'Assets' / 'images' / 'pink_laser.png'
        self.bullet_file_pb = Path.cwd() / 'Assets' / 'images' / 'p_b_laser.png'
        self.bullet_file_red = Path.cwd() / 'Assets' / 'images' / 'red_laser.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser7.mp3'
        self.bullet_speed = 7
        self.bullet_w = 24
        self.bullet_h = 24
        self.bullet_amount = 5

        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'alien.png'
        self.alien_w = 72
        self.alien_h = 72
        self.fleet_speed = 2
        self.fleet_direction = 1