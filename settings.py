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
        bullet_file_pb (file)
            file for bullet image
        laser_sound (file)
            file for sound played when bullet is fired
        impact_sound (file)
            file for sound played when a collision between laser and alien 
            occurs
        bullet_speed (int)
            sets speed of the bullet (laser)
        bullet_w (int)
            width of bullet image
        bullet_h (int)
            height of bullet image
        bullet_amount (int)
            amount of bullets allowed on screen
        alien_file (file)
            image used for alien
        alien_w (int)
            width of alien image
        alien_h (int)
            height of alien image
        fleet_speed (int)
            speed on which fleet of aliens move
        fleet_direction (int)
            int that changes to negative to move in the opposite direction
        fleet_drop_speed (int)
            the y value used to make the alien fleet drop down when boundary is
            hit

        """
        self.name: str = "Alien Invasion"
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'space.png'
        self.difficulty_scale = 1.1
        self.alien_size_scale = 2
        self.scores_file = Path.cwd() / 'Assets' / 'file' / 'scores.json'

        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'spaceship.png'
        self.ship_w = 64
        self.ship_h = 64

        # self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'green_laser2.png'
        # self.bullet_file_pink = Path.cwd() / 'Assets' / 'images' / 'pink_laser.png'
        # self.bullet_file_red = Path.cwd() / 'Assets' / 'images' / 'red_laser.png'
        self.bullet_file_pb = Path.cwd() / 'Assets' / 'images' / 'p_b_laser.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser7.mp3'
        self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'explosion.mp3'
        self.title_screen_music = Path.cwd() / 'Assets' / 'sound' / 'Battle in the Stars.mp3'

        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'alien.png'
        self.fleet_direction = 1

        self.button_w = 200
        self.button_h = 50
        self.button_color = (167, 66, 245)

        self.text_color = (255, 255, 255)
        self.button_font_size = 48
        self.HUD_font_size = 20
        self.font_file = Path.cwd() / 'Assets' / 'Fonts' / 'Silkscreen' / 'PixelifySans-VariableFont_wght.ttf'

    def initialize_dynamic_settings(self):

        self.ship_speed = 5
        self.starting_ship_count = 3
        
        self.bullet_w = 24
        self.bullet_h = 24
        self.bullet_speed = 7
        self.bullet_amount = 5

        self.alien_w = 56
        self.alien_h = 56

        self.fleet_speed = 2
        self.fleet_drop_speed = 36

        self.alien_points = 50

    def increase_difficulty(self):
        self.ship_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale
        self.alien_w -= self.alien_size_scale
        self.alien_h -= self.alien_size_scale