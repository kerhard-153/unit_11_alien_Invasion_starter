import pygame.font

from typing import TYPE_CHECKING

if TYPE_CHECKING:
   from alien_invasion import AlienInvasion

class Button:

    """
    Manages all aspects of the "Start" button

    Methods
    -------

    __init__(self, game: 'AlienInvasion', msg)
        Initializes button attributes
    _prep_msg(self.msg)
        renders and centers message image
    draw(self)
        draws the button on the screen
    check_clicked(self, mouse_pos)
        checks if the button was clicked
    """

    def __init__(self, game: 'AlienInvasion', msg):

        """
        Initializes button attributes

        Args
        ----
        game: AlienInvasion
        msg: text inside the button

        Attributes
        ----------
        game
            AlienInvasion
        screen
            screen of game
        settings
            references the settings file
        boundaries
            gets a rect of the screen to establish boundaries
        font
            creates the font from the font file and size
        rect
            creates the buttom from button width and height
        
        Calls
        -----

        _prep_message(Arg: msg)
            renders and centers message in the button
        """
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.boundaries = game.screen.get_rect()

        self.font = pygame.font.Font(self.settings.font_file,
             self.settings.button_font_size)
        self.rect = pygame.Rect(0,0, self.settings.button_w, self.settings.button_h)
        self.rect.center = self.boundaries.center
        self._prep_msg(msg)

    def _prep_msg(self, msg):

        """
        Renders message as an image and centers message in the button rect

        Args
        ----
        msg (str)
            word(s) that appear in the button
        """
        self.msg_image = self.font.render(msg, False, self.settings.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):

        """
        Draws button and message image on the screen
        """
        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def check_clicked(self, mouse_pos):

        """
        Checks if the button is clicked

        Args
        ----

        mouse_pos
            position of players mouse

        Returns
        -------
            bool: if the rect and mouse_pos have collided
        """
        return self.rect.collidepoint(mouse_pos)