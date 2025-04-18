import pygame.font

# from alien_invasion import AlienInvasion
# from typing import TYPE_CHECKING

# if TYPE_CHECKING:

class HUD:
   
    def __init__(self, game):
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
        self.life_image = pygame.image.load(self.settings.ship_file)
        self.life_image = pygame.transform.scale(self.life_image, 
            (self.settings.ship_w, self.settings.ship_h))
        
        self.life_rect = self.life_image.get_rect()


    def update_scores(self):
        self._update_score()
        self._update_max_score()
        self._update_hi_score()

    def _update_score(self):
        score_str = f'SCORE: {self.game_stats.score: ,.0f}'
        self.score_image = self.font.render(score_str, True, 
            self.settings.text_color, None)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.boundaries.right - self.margin
        self.score_rect.top = self.score_rect.bottom + self.margin
    
    def _update_max_score(self):
        max_score_str = f'MAX-SCORE: {self.game_stats.max_score: ,.0f}'
        self.max_score_image = self.font.render(max_score_str, True, 
            self.settings.text_color, None)
        self.max_score_rect = self.max_score_image.get_rect()
        self.max_score_rect.right = self.boundaries.right - self.margin
        self.max_score_rect.top = self.margin
    
    def _update_hi_score(self):
        hi_score_str = f'HI-SCORE: {self.game_stats.hi_score: ,.0f}'
        self.hi_score_image = self.font.render(hi_score_str, True, 
            self.settings.text_color, None)
        self.hi_score_rect = self.hi_score_image.get_rect()
        self.hi_score_rect.midtop = (self.boundaries.centerx, self.margin)

    def update_level(self):
        level_str = f'LEVEL: {self.game_stats.level: ,.0f}'
        self.level_image = self.font.render(level_str, True, 
            self.settings.text_color, None)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.margin
        self.level_rect.top = self.life_rect.bottom + self.margin

    def _draw_lives(self):
        current_x = self.margin
        current_y = self.margin
        for _ in range(self.game_stats.ships_left):
            self.screen.blit(self.life_image, (current_x, current_y))
            current_x += self.life_rect.width + self.margin

    def draw(self):
        self.screen.blit(self.hi_score_image, self.hi_score_rect)
        self.screen.blit(self.max_score_image, self.max_score_rect)
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self._draw_lives()
       
    