import pygame
from typing import TYPE_CHECKING
from bullet import Bullet

if TYPE_CHECKING:
   from alien_invasion import AlienInvasion
   

class ShipArsenal:

    """
    Creates the aresenal that the ship uses to fire bullets

    Methods
    -------

    __init__
        initializes elements in reference to 'AlienInvasion'
    update_arsenal()
        updates arsenal and bullets
    _remove_bullets_offscreen()
        removes bullets if the leave the screen
    draw()
        draws bullets on the screen
    fire_bullet()
        fires the bullet from the ship
    """

    def __init__(self, game: 'AlienInvasion'):
        """
        Initializes elements for the arsenal

        Args
        ----
            game (AlienInvasion): Alien Invasion game

        Attributes
        ----------

        game
            AlienInvasion
        settings
            class: Settings
        arsenal
            creates sprite group
        """
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self):
        """
        Updates arsenal and bullets

        Calls
        -----
        _remove_bullets_offscreen()
        
        """
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self):

        """
        Removes bullets when the bottom of rect is no longer on screen

        Iterates through copy of the list to prevent unwanted changes
        """
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)


    def draw(self):

        """
        Draws the bullet on the screen

        Calls
        -----

        draw.bullet() from bullet
        """
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self):

        """
        Adds new bullet if the allowed amount of bullets has not been reached

        Returns:
            True: If length of arsenal is less than bullet_amount from settings
        """
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False