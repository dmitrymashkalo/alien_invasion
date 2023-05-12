class GameStats:
    """ Class for tracking stats for the game """

    def __init__(self, ai_game):
        """ Init static game stats """
        self.settings = ai_game.settings

        # Load last record from file if exists from the txt file
        self.filename = 'record_table.txt'
        self.high_score = self.load_record()

        # Init dynamic game stats
        self.reset_stats()

        # Game starts flag
        self.game_active = False


    def reset_stats(self):
        """ Init dynamic game stats """
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.lvl = 1


    def save_record(self):
        """ Save high score result in the txt file """
        with open(self.filename, 'w') as file:
            file.write(str(self.high_score))


    def load_record(self):
        """ Load existing result from the txt file if exists"""
        try:
            with open(self.filename) as file:
                self.last_record = file.read()
        except:
            self.last_record = 0
        
        return int(self.last_record)
