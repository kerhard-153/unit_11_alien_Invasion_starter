import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
   from alien_fleet import AlienFleet

class Alien(Sprite):

    """
    Class for alien sprites (enemy)

    Methods
    -------

    __init__
        initializes elements of the alien "fleet"
    update
        updates speed of aliens on screen
    check_edges
        checks for the edge of the screen
    draw_alien
        draws the alien on the screen
    """
   
    def __init__(self, fleet: 'AlienFleet', x: float, y: float):
        super().__init__()

        """
        Initializes elements of the alien and fleet

        Args
        ----

        fleet
            class AlienFleet from file alien_fleet
        x (float)
            x-coordinate (used by rect)
        y (float)
            y-coordinate (used by rect)

        Attributes
        ----------

        fleet
            group fo aliens moving toward bottom of the screen
        image
            image file of alien
            scaled by width and height from settings
        rect
            creates rect for each alien
        """
        
        self.fleet = fleet
        self.screen = fleet.game.screen
        self.boundaries = fleet.game.screen.get_rect()
        self.settings = fleet.game.settings

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.alien_w, self.settings.alien_h)
            )

        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):

        """
        Updates speed and direction of the fleet

        Attributes
        ----------

        temp_speed (int)
            speed of fleet from settings
        x
            determines speed and direction of fleet movement
        """
        temp_speed = self.settings.fleet_speed

        self.x += temp_speed * self.fleet.fleet_direction
        self.rect.x = self.x
        self.rect.y = self.y

    def check_edges(self):
       
        """
        Checks for hitting the edges of the screen

        Returns:
            True: if edge of screen is hit
            False: if edge of screen is not hit
        """
        return (self.rect.right >= self.boundaries.right or self.rect.left <= self.boundaries.left)
        

    def draw_alien(self):

        """
        Draws alien on the screen

        Methods
        -------

        blit(Args: image, rect)
        """
        self.screen.blit(self.image, self.rect)