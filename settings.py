class Settings:
    """This class store all Alien Invasion settings."""

    def __init__(self):
        "Init game settings"
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.name = "Alien Invasion"
        self.background_color = (230, 230, 230)

        # Bullet settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 60, 60)
        self.bullet_allowed = 3

        # Ship settings
        self.ship_speed = 1.5
