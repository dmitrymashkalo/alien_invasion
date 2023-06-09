class Settings:
    """ This class store all game settings """

    def __init__(self):
        """ Init static game settings """
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_name = "Alien Invasion"
        self.background_color = (230, 230, 230)
        self.text_color = (60, 60, 60)
        self.full_screen_mode = True

        # Bullet settings
        self.bullet_width = 10
        self.bullet_height = 25
        self.bullet_color = (255, 60, 60)
        self.bullet_allowed = 3

        # Ship settings
        self.ship_limit = 3

        # Aliens settings
        self.fleet_drop_speed = 20

        # Game acceleration rate
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        # Init dynamic settings
        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """ Init dynamic game settings """
        # Init speed settings
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # Change direction. fleet_direction = 1 is right, -1 is left
        self.fleet_direction = 1

        # Score
        self.alien_points = 15


    def increase_speed(self):
        """ Increases game values """
        # Increases the speed of the ship, aliens and bullets
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        # Increases score points
        self.alien_points = int(self.alien_points * self.score_scale)
