class GameStats:
    """ Class for tracking stats for the game """

    def __init__(self, ai_game):
        """ Init stats """
        self.settings = ai_game.settings
        self.reset_stats()

        # Game starts in active state
        self.game_active = False


    def reset_stats(self):
        """ Init stats that changed during the game """
        self.ships_left = self.settings.ship_limit