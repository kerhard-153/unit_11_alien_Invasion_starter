from typing import TYPE_CHECKING

if TYPE_CHECKING:
   from alien_invasion import AlienInvasion

class GameStats():

    """
    Tracks game status

    Functions
    ---------

    __init__
        initializes status of elements of the game

    """

    def __init__(self, game: 'AlienInvasion'):

        """
        Initializes elements of the game to track

        Attributes
        ----------

        ships_left (int)
            the amount of ships avalible before "game over"
        """
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1


    def update(self, collisions):
        self._update_score(collisions)

        self._update_max_score()

    def _update_max_score(self):
        if self.score > self.max_score:
            self.max_score = self.score

    def _update_score(self, collisions):
        for alien in collisions.values():
            self.score += self.settings.alien_points

    def update_level(self):
        self.level += 1
        print(self.level)


