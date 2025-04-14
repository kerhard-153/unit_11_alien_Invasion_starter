class GameStats():

    """
    Tracks game status

    Functions
    ---------

    __init__
        initializes status of elements of the game

    """

    def __init__(self, ships_left):

        """
        Initializes elements of the game to track

        Attributes
        ----------

        ships_left (int)
            the amount of ships avalible before "game over"
        """
        self.ships_left = ships_left
