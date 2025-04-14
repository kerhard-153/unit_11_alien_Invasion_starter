import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
   from alien_invasion import AlienInvasion

class Bullet(Sprite):

    """
    Creates, updates, and draws the bullet(laser) on the screen

    Methods
    -------

    __init__
        Initializes bullet, image and rect
    update()
        updates bullet and rect
    draw_bullet()
        draws bullet on screen

    """
   
    def __init__(self, game: 'AlienInvasion'):

        """
        Initializes bullet, image, and rect

        Attributes
        ----------

        image
            bullet file from settings
            scales it based on width and height from settings
        rect
            creates rect for the bullet
            positions bullet at midtop of the ship
        """
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.bullet_file_pb)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.bullet_w, self.settings.bullet_h)
            )

        
        self.rect = self.image.get_rect()
        self.rect.midtop = game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):

        """
        Updates bullet on screen

        Attributes
        ----------

        y
            holds the speed of the bullet, moves upward due to decrease in y 
            value
        """
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """
        Draws bullet on screen

        Methods
        -------
        blit(Args: image, rect)
        """
        self.screen.blit(self.image, self.rect)