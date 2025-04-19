import pygame
from alien import Alien
from typing import TYPE_CHECKING

if TYPE_CHECKING:
   from alien_invasion import AlienInvasion
   

class AlienFleet:

    """
    Manages the alien fleet

    Methods
    -------
    __init__(self, game: 'AlienInvasion')
        Initializes attributes of the alien fleet
    create_fleet(self) 
        Creates the alien fleet
    _create_trapezoid_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset)
        Creates the alien fleet in the shape of a trapezoid
    calc_offsets(self, alien_w, alien_h, screen_w, fleet_w, fleet_h)
        Calculates the distance between the fleet and the edge of the screen
    calc_fleet_size(self, alien_w, screen_w, alien_h, screen_h)
        Calculates the size of the fleet based on the screen
    _create_alien(self, current_x: int, current_y: int)
        Creates an alien and adds it to the fleet
    check_fleet_edges(self)
        Checks each alien for a collision with the edge of the screen. If the 
        edge is hit, the fleet moves downward and changes horizontal direction
    drop_alien_fleet(self)
        Drops the alien fleet vertically
    update_fleet(self)
        Updates fleet and checks if fleet collides with edges of screen 
    draw(self)
        Draws the aliens in the fleet on the screen
    check_collisions(self, other_group)
        Checks for collisions between the aliens and another group
    check_fleet_bottom(self)
        Checks for a collision between an alien in the fleet and the bottom of
        the screen
    check_destroyed_status(self)
        Checks if fleet has been destroyed, returns that fleet has been destroyed
    

    """
   
    def __init__(self, game: 'AlienInvasion'):

        """
        Initializes attributes of the alien fleet

        Args
        ----

        game: AlienInvasion

        Attributes
        ----------

        settings
            references settings file
        fleet
            creates a sprite group
        fleet_direction
            value of 1 or -1 to move in a direction across the x-axis
        fleet_drop_speed
            the speed at which the fleet moves down the y-axis when a boundary 
            is hit

        Calls
        -----
        create_fleet()
            creates the alien fleet
       

        """
        
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        self.create_fleet()

    def create_fleet(self):

        """
        Creates the alien fleet

        Attributes
        ----------
        alien_w
            width of alien
        alien_h
            height of alien
        screen_w
            width of screen
        screen_h
            height of screen

        Calls
        -----
        calc_fleet_size(Args: alien_w, alien_h, screen_w, screen_h)
            calculates the size of the fleet
        calc_offsets(Args: alien_w, alien_h, screen_w, fleet_w, fleet_h)
            calculates how far away the fleet will be from the edge of the screen
        _create_trapezoid_fleet(Args: alien_w, alien_h, fleet_w, fleet_h, 
        x_offset, y_offset)
            creates the shape of the alien fleet
        """
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_w = self.settings.screen_w
        screen_h = self.settings.screen_h

        fleet_w, fleet_h = self.calc_fleet_size(alien_w, screen_w, alien_h, screen_h)

        x_offset, y_offset = self.calc_offsets(alien_w, alien_h, screen_w, fleet_w, fleet_h)

        self._create_trapezoid_fleet(alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset)

    def _create_trapezoid_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):

        """
        Creates the alien fleet in the shape of a trapezoid

        Attributes
        ----------

        current_x
            x position of the alien
        current_y
            y position of the alien

        Calls
        -----
        _create_alien(Args: current_x, current_y)
            creates the alien based on the current x and y position
        """
        for row in range(fleet_h):
            for col in range(row, fleet_w - row):
                current_x = alien_w * col + x_offset
                current_y = alien_h * row + y_offset

                self._create_alien(current_x, current_y)

     

    def calc_offsets(self, alien_w, alien_h, screen_w, fleet_w, fleet_h):

        """
        Calculates the distance between the fleet and the edge of the screen

        Returns
        -------
            x_offset: horizontal distance from the edge of the screen 
            y_offset: vertical distance from the edge of the screen 
        """
        half_screen = self.settings.screen_h // 2
        fleet_horizontal_space = fleet_w * alien_w
        fleet_vertical_space = fleet_h * alien_h
        x_offset = int((screen_w - fleet_horizontal_space)//2)
        y_offset = int((half_screen - fleet_vertical_space)//2)
        return x_offset,y_offset
    

    def calc_fleet_size(self, alien_w, screen_w, alien_h, screen_h):

        """
        Calculates the size of the fleet based on the screen

        Attributes
        ----------
        fleet_w
            number of columns in the alien fleet
        fleet_h
            number of rows in the alien fleet

        Returns:
            fleet_w (int): rows that fit on screen
            fleet_h (int): cols that fit on screen
        """
        fleet_w = (screen_w//alien_w)
        fleet_h = ((screen_h /2)// alien_h)

        if fleet_w % 2 == 0:
            fleet_w -= 1
        else:
            fleet_w -= 2
        
        if fleet_h % 2 == 0:
            fleet_h -= 1
        else:
            fleet_h -= 2
        
        return int(fleet_w), int(fleet_h)
    
    def _create_alien(self, current_x: int, current_y: int):

        """
        Creates an alien and adds it to the fleet

        Args
        ----
        current_x
            x position of alien
        current_y
            y position of alien

        
        """
        new_alien = Alien(self, current_x, current_y)

        self.fleet.add(new_alien)

    def check_fleet_edges(self):

        """
        Checks each alien for a collision with the edge of the screen. If the 
        edge is hit, the fleet moves downward and changes horizontal direction
        """
        alien: Alien
        for alien in self.fleet:
            if alien.check_edges():
                self.drop_alien_fleet()
                self.fleet_direction *= -1
                break

    def drop_alien_fleet(self):

        """
        Drops the alien fleet vertically
        """
        for alien in self.fleet:
            alien.y += self.fleet_drop_speed

    def update_fleet(self):

        """
        Updates fleet and checks if fleet collides with edges of screen
        """
        self.check_fleet_edges()
        self.fleet.update()

    def draw(self):
        """
        Draws the aliens in the fleet on the screen
        """
        alien: 'Alien'
        for alien in self.fleet:
            alien.draw_alien()

    def check_collisions(self, other_group):

        """
        Checks for collisions between the aliens and another group

        Args
        ----
        other_group
            a separate group with the potential to collide with an alien

        Returns:
            bool: True or False if a collision occurs
        """
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)
    
    def check_fleet_bottom(self):

        """
        Checks for a collision between an alien in the fleet and the bottom of
        the screen
        """      
        for alien in self.fleet:
            if alien.rect.bottom >= self.settings.screen_h:
                return True
        return False
    
    def check_destroyed_status(self):

        """
        Checks if fleet has been destroyed, returns that fleet has been destroyed

        """
        return not self.fleet
    
