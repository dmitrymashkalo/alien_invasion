class GameStats:
    """ Class for tracking stats for the game """

    def __init__(self, ai_game):
        """ Init stats """
        self.settings = ai_game.settings

        # Load last record from file if exists
        self.filename = 'record_table.txt'
        self.high_score = self.load_record()

        self.reset_stats()

        # Game starts in active state
        self.game_active = False


    def reset_stats(self):
        """ Init stats that changed during the game """
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.lvl = 1

    def save_record(self):
        with open(self.filename, 'w') as file:
            file.write(str(self.high_score))

    def load_record(self):
        try:
            with open(self.filename) as file:
                self.last_record = file.read()
        except:
            self.last_record = 0
        
        return int(self.last_record)