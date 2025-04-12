import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
   from alien_invasion import AlienInvasion 
   from arsenal import ShipArsenal

class Ship:
    """
    Initializes the ship and handles in-game activities

    Functions
    ---------
    __init__(self, game: 'AlienInvasion')
        initializes rect for the ship image and its movements
    update(self)
        sets ship speed, prevents ship from leaving the screen
    draw(self)
        places the ship image on the screen
    
    """   
    
    def __init__(self, game: 'AlienInvasion', arsenal: 'ShipArsenal'):

        """
        Initializes ship elements
        Establishes rect for the screen and ship image, loads and trasforms the 
        ship image to scale, places the image at the mid-bottom of the screen, 
        and initializes variables for moving ship across the x-axis.

        Parameters
        ----------
        game ('AlienInvasion')
            refers to the main game class

        
        """
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale( self.image, 
            (self.settings.ship_w, self.settings.ship_h)
            )
        self.rect = self.image.get_rect()
        self._center_ship()
        self.moving_right = False
        self.moving_left = False
        self.arsenal = arsenal

    def _center_ship(self):
        self.rect.midbottom = self.boundaries.midbottom
        self.x = float(self.rect.x)
    
    def update(self):

        """
        Sets the speed of the ship and prevents it from exiting the edges of 
        the screen

        Attributes
        ----------
        ship_x_speed (int)
            references the settings file for the speed of the ship

        """
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        ship_x_speed = self.settings.ship_speed
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += ship_x_speed
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= ship_x_speed

        self.rect.x = self.x


    def draw(self):
        """
        Places the ship on the screen

        Attributes
        ----------
        image, rect
            initialized in the __init__ function
        """
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self):
        return self.arsenal.fire_bullet()
    
    def check_collisions(self, other_group):
        if pygame.sprite.spritecollideany(self, other_group):
            self._center_ship()
            return True
        return False