import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import ShipArsenal
from alien_fleet import AlienFleet
from game_stats import GameStats
from time import sleep

class AlienInvasion:
    """
    Manage game assets and behaviors
    
    ...

    Attributes
    ----------

    screen (int)
        sets the screen width and height, imported from settings
    bg (file)
        sets the screen background, imported from settings
    running (bool)
        determines if the game is running 
    clock (int)
        represents the FPS of that game
    ship (object)
        the "character" that the player can control

    Functions
    ---------

    __init__(self)
        initializes elements of the game
    run_game(self)
        the game loop
    _update_screen(self)
        updates the screen (backgound and drawing the ship)
    _check_events(self)
        checks events of player 
    _check_keydown_events(self, event)
        moves the character left or right, or quits the game based on key 
        pressed
    _check_keyup_events(self, event)
        stops moving character when key is released

    """

    def __init__(self):

        """
        Initializes elements of the game

        Attributes
        ----------

        settings (class)
            imports Settings() class from file
        screen (int)
            sets the screen width and height, imported from settings
        bg (file)
            sets the screen background, imported from settings
        running (bool)
            determines if the game is running 
        clock (int)
            represents the FPS of that game
        ship (object)
            the "character" that the player can control

        Methods
        -------

        set_mode() 
            sets screen width and height
        set_caption()
            sets caption of the game for player to see
        load()
            loads the background
        scale()
            scales background to fit the screen

        
        """
        
        pygame.init()
        self.settings = Settings()
        self.game_stats = GameStats(self.settings.starting_ship_count)

        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
            )
        pygame.display.set_caption(self.settings.name)
        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, 
            (self.settings.screen_w, self.settings.screen_h)
            )

        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.5)
        self.impact_sound = pygame.mixer.Sound(self.settings.impact_sound)
        self.impact_sound.set_volume(0.2)

        self.ship = Ship(self, ShipArsenal(self))
        self.alien_fleet = AlienFleet(self)
        self.alien_fleet.create_fleet()
        self.game_active = True

    def run_game(self): 

        """
        Game loop, runs the game while self.running == True
        
        Calls
        -----
        _check_events()
        update()
        _update_screen()

        Methods
        -------

        tick()
            runs the game at specified FPS (access through settings)
        """  
        while self.running:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self.alien_fleet.update_fleet()
                self._check_collisions()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_collisions(self):

        # check collisions for ship
        if self.ship.check_collisions(self.alien_fleet.fleet):
            self._check_game_status()

         # checkcollisions for aliens and bottom of the screen
        if self.alien_fleet.check_fleet_bottom():
            self._check_game_status()

        # check collisions of projectiles and aliens
        collisions = self.alien_fleet.check_collisions(self.ship.arsenal.arsenal)
        if collisions:
            self.impact_sound.play()
            self.impact_sound.fadeout(500)

        if self.alien_fleet.check_destroyed_status():
            self._reset_level()

    def _check_game_status(self):
        if self.game_stats.ships_left > 0:
            self.game_stats.ships_left -= 1
            self._reset_level()
            sleep(1.0)
        else:
            self.game_active = False
        
        print(self.game_stats.ships_left)

    def _reset_level(self):
        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()

    def _update_screen(self):

        """
        Updates game screen while game is running

        Methods
        -------

        blit()
            places background image on the screen
        draw()
            draws the ship onto the screen
        flip()
            updates the game screen
        """
        self.screen.blit(self.bg, (0, 0))
        self.ship.draw()
        self.alien_fleet.draw()
        pygame.display.flip()

    def _check_events(self): 

        """
        Checks events while game is running, quits player exits the window

        Calls
        -----

        _check_keydown_events(Arg: event)
            checks if player presses a key
        _check_keyup_events(Arg: event)
            checks if player releases a key

        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):

        """
        When player presses a key, an action is performed

        Args
        ----

        event
            a key is pressed
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()
    def _check_keyup_events(self, event):

        """
        When player presses a key, an action is performed

        Args
        ----

        event
            a key is pressed
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

            


if __name__ == '__main__':

    """
    Main function

    Calls
    -----
    run_game()
        runs game from AlienInvasion class
    """
    
    alien_inv = AlienInvasion()
    alien_inv.run_game()
