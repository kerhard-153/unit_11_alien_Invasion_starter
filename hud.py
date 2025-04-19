import pygame.font


class HUD:

    """
    Creates the HUD

    Methods
    -------

    __init__(self, game)
        Initializes HUD attributes
    _setup_life_image(self)
        sets up image to show the player "lives"
    update_scores(self)
        updates score, max_score, and hi_score on screen
    _update_score(self)
        updates current score on screen
    _update_max_score(self)
        updates max score on screen
    _update_hi_score(self)
        updates hi score on screen
    update_level(self)
        updates level on screen
    _draw_lives(self)
        draws life image on screen
    draw(self)
        draws all HUD elements
    """
   
    def __init__(self, game):

        """
        Initializes attributes of the HUD

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
        game_stats
            game stats file
        font
            references font file and size for the HUD
        margin
            space from the edges of the screen
        
        """
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.game_stats = game.game_stats
        self.font = pygame.font.Font(self.settings.font_file, 
                self.settings.HUD_font_size)
        self.margin = 30
        self.update_scores()
        self._setup_life_image()
        self.update_level()

    def _setup_life_image(self):

        """
        Sets up image ro represent player lives on the HUD

        Attributes
        ----------
        life_image
            loads and scales ship file as an image
        """
        self.life_image = pygame.image.load(self.settings.ship_file)
        self.life_image = pygame.transform.scale(self.life_image, 
            (self.settings.ship_w, self.settings.ship_h))
        
        self.life_rect = self.life_image.get_rect()


    def update_scores(self):

        """
        Updates score, max score, and hi score on HUD
        """
        self._update_score()
        self._update_max_score()
        self._update_hi_score()

    def _update_score(self):

        """
        Updates score on HUD

        Attributes
        ----------

        score_str (str)
            text used to indicate score
        score_image 
            renders score str as an image
        score_rect
            gets rect for score image and positions it
        """
        score_str = f'SCORE: {self.game_stats.score: ,.0f}'
        self.score_image = self.font.render(score_str, True, 
            self.settings.text_color, None)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.boundaries.right - self.margin
        self.score_rect.top = self.score_rect.bottom + self.margin
    
    def _update_max_score(self):

        """
        Updates max score on HUD

        Attributes
        ----------

        max_score_str (str)
            text used to indicate max score
        max_score_image 
            renders max score str as an image
        max_score_rect
            gets rect for max score image and positions it
        """

        max_score_str = f'MAX-SCORE: {self.game_stats.max_score: ,.0f}'
        self.max_score_image = self.font.render(max_score_str, True, 
            self.settings.text_color, None)
        self.max_score_rect = self.max_score_image.get_rect()
        self.max_score_rect.right = self.boundaries.right - self.margin
        self.max_score_rect.top = self.margin
    
    def _update_hi_score(self):

        """
        Updates hi score on HUD

        Attributes
        ----------

        hi_score_str (str)
            text used to indicate hi score
        hi_score_image 
            renders hi score str as an image
        hi_score_rect
            gets rect for hi score image and positions it
        """

        hi_score_str = f'HI-SCORE: {self.game_stats.hi_score: ,.0f}'
        self.hi_score_image = self.font.render(hi_score_str, True, 
            self.settings.text_color, None)
        self.hi_score_rect = self.hi_score_image.get_rect()
        self.hi_score_rect.midtop = (self.boundaries.centerx, self.margin)

    def update_level(self):

        """
        Updates level on HUD

        Attributes
        ----------

        level_str (str)
            text used to indicate level
        level_image 
            renders level str as an image
        level_rect
            gets rect for level image and positions it
        """
        level_str = f'LEVEL: {self.game_stats.level: ,.0f}'
        self.level_image = self.font.render(level_str, True, 
            self.settings.text_color, None)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.margin
        self.level_rect.top = self.life_rect.bottom + self.margin

    def _draw_lives(self):

        """
        Draws ships on screen to indicate lives

        Attributes
        ----------

        current_x
            x position of image
        curent_y
            y position of image
        
        """
        current_x = self.margin
        current_y = self.margin
        for _ in range(self.game_stats.ships_left):
            self.screen.blit(self.life_image, (current_x, current_y))
            current_x += self.life_rect.width + self.margin

    def draw(self):

        """
        Draws hi score, max score, score, and level images on the screen
        """
        self.screen.blit(self.hi_score_image, self.hi_score_rect)
        self.screen.blit(self.max_score_image, self.max_score_rect)
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self._draw_lives()
       
    