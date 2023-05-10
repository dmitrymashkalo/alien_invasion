class Settings:
    """ This class store all game settings """

    def __init__(self):
        """ Initializing game settings """
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_name = "Alien Invasion"
        self.background_color = (230, 230, 230)
        self.full_screen_mode = True

        # Bullet settings
        self.bullet_speed = 2
        self.bullet_width = 9
        self.bullet_height = 25
        self.bullet_color = (255, 60, 60)
        self.bullet_allowed = 3

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Aliens settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 40

        # fleet_direction = 1 is right, -1 is left
        self.fleet_direction = 1
