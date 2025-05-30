import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import ShipArsenal
from alien_fleet import AlienFleet
from game_stats import GameStats
from time import sleep
from button import Button
from hud import HUD

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
    play_background_music(self)
        plays the background music of the game
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
        self.settings.initialize_dynamic_settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
            )
        pygame.display.set_caption(self.settings.name)
        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, 
            (self.settings.screen_w, self.settings.screen_h)
            )

        self.game_stats = GameStats(self)
        self.HUD = HUD(self)
        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.5)
        self.impact_sound = pygame.mixer.Sound(self.settings.impact_sound)
        self.impact_sound.set_volume(0.3)
        self.lose_ship_sound = pygame.mixer.Sound(self.settings.lose_ship_sound)
        self.lose_ship_sound.set_volume(0.5)
        self.play_background_music()

        self.ship = Ship(self, ShipArsenal(self))
        self.alien_fleet = AlienFleet(self)
        self.alien_fleet.create_fleet()
        self.play_button = Button(self, 'START')
        self.game_active = False

    def play_background_music(self):

        """
        Plays background music

        Attributes
        ----------

        title_screen_music
            loads music file from settings

        """
        self.title_screen_music = pygame.mixer.music.load(
            self.settings.title_screen_music)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)

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

        """
        Checks for collisions for the ship, aliens and the bottom of the screen,
        and between the projectiles and aliens. 

        Methods
        -------

        check_collisions()
            checks for collisions between sprites
        _check_game_status()
            checks for remaining ships, resets, level, and contains sleep timer
        check_fleet_bottom()
            checks for bottom of the alien fleet
        check_destroyed_status()
            checks if alien fleet is destroyed
        update (Args: collisions)
            updates game stats based on collisions
        update_scores()
            updates the scores on the HUD
        _reset_level()
            resets level when fleet is destroyed
        increase_difficulty()
            increases difficulty when alien fleet is destroyed
        update_level()
            game_stats: increments level by 1
            HUD: updates level display
        
         
        """

        if self.ship.check_collisions(self.alien_fleet.fleet):
            self._check_game_status()

        if self.alien_fleet.check_fleet_bottom():
            self._check_game_status()

        collisions = self.alien_fleet.check_collisions(self.ship.arsenal.arsenal)
        if collisions:
            self.impact_sound.play()
            self.impact_sound.fadeout(500)
            self.game_stats.update(collisions)
            self.HUD.update_scores()

        if self.alien_fleet.check_destroyed_status():
            self._reset_level()
            self.settings.increase_difficulty()
            self.game_stats.update_level()
            self.HUD.update_level()


    def _check_game_status(self):

        """
        Checks for status of elements in the game

        Decrements ships_left if collision between aliens and the bottom of the
        screen or aliens and the ship occurs, as well as resets the level
        """
        if self.game_stats.ships_left > 0:
            pygame.mixer.music.pause()
            self.lose_ship_sound.play()
            self.game_stats.ships_left -= 1
            self._reset_level()
            sleep(1.0)
            pygame.mixer.music.unpause()
        else:
            self.game_active = False
        

    def _reset_level(self):

        """
        Resets the level, empties the screen and recreates all elements
        """
        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()


    def restart_game(self):

        """
        Restarts all elements of the game to where they were, preserving only 
        the high score
        """

        self.settings.initialize_dynamic_settings()
        self.game_stats.reset_stats()
        self.HUD.update_scores()
        self._reset_level()
        self.ship._center_ship()
        self.game_active = True
        pygame.mouse.set_visible(False)

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
        self.HUD.draw()

        if not self.game_active:
            self.play_button.draw()
            pygame.mouse.set_visible(True)

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
        _check_button_clicked()
            checks if player clicked the "start" button

        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.game_stats.save_scores()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and self.game_active == True:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_button_clicked()

    def _check_button_clicked(self):

        """
        Checks if player clicks the "start" button, prepares screen for the 
        start of the game

        Attributes
        ----------

        mouse_pos
            gets mouse position of the player
        """
        mouse_pos = pygame.mouse.get_pos()
        if self.play_button.check_clicked(mouse_pos):
            self.restart_game()
            pygame.mixer.music.set_volume(0.3)

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
            self.game_stats.save_scores()
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
