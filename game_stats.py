
import json

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

        game
            AlienInvasion
        settings
            settings file for game
        max_score
            initializes max score as 0
        
        Methods
        -------

        init_saved_scores
            retrieves hi score fron json file if it exists, creates file if not

        """
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.init_saved_scores()
        self.reset_stats()

    def init_saved_scores(self):

        """
        Retrieves hi score fron json file if it exists, creates file if not and
        sets hi score to 0
        """
        self.path = self.settings.scores_file
        if self.path.exists() and self.path.stat.__sizeof__() > 20:
            contents = self.path.read_text()
            scores = json.loads(contents)
            self.hi_score = scores.get('hi_score', 0)
        else:
            self.hi_score = 0
            self.save_scores()

    def save_scores(self):

        """
        Saves hi score in json file

        Exceptions
        ----------

        FileNotFoundError
            if json file does not exist
        """
        scores = {
            'hi_score' : self.hi_score
        }
        contents = json.dumps(scores, indent=4)
        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f'File Not Found: {e}')


    def reset_stats(self):

        """
        Resets stats to the starting stats

        Attributes
        ----------

        ships_left (int)
            the amount of ships avalible before "game over"
        score(int)
            sets score back to 0
        level(int)
            sets level back to 1
        """
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1


    def update(self, collisions):

        """
        Updates score, max_score, and hi score
        """
        self._update_score(collisions)

        self._update_max_score()

        self._update_hi_score()

    def _update_max_score(self):

        """
        Updates max score as the player is earning points if the score is greater
        than the max score
        """
        if self.score > self.max_score:
            self.max_score = self.score
    
    def _update_hi_score(self):

        """
        Updates hi score as the player is earning points if the score is greater
        than the hi score
        """
        if self.score > self.hi_score:
            self.hi_score = self.score

    def _update_score(self, collisions):
        

        """
        Updates score when an alien is destroyed, adds points to the score
        """
        for alien in collisions.values():
            self.score += self.settings.alien_points

    def update_level(self):

        """
        Increments the level number by 1 if fleet is destroyed
        """
        self.level += 1



