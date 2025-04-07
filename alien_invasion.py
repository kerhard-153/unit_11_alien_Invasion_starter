import sys
import pygame
from settings import Settings
from ship import Ship

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

        self.ship = Ship(self)

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
            self.ship.update()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

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
