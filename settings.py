class Settings:
    """This class store all Alien Invasion settings."""

    def __init__(self):
        "Init game settings"
        self.screen_width = 1200
        self.screen_height = 800
        self.name = "Alien Invasion"
        self.background_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 0.8
