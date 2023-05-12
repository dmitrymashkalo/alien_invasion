import pygame.font
from pygame.sprite import Group
from health import Health


class Scoreboard:
    """ Class for displaing game info """

    def __init__(self, ai_game):
        """ Init scoring attributes """
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Init font
        self.font = pygame.font.SysFont(None, 48)
        
        # Preparing scoring images
        self.prep_score()
        self.prep_high_score()
        self.prep_lvl()
        self.prep_health()

    
    def prep_score(self):
        """ Converts the current score to an image """
        # Rounded the integer
        rounded_score = round(self.stats.score)
        # Forming string
        score_str = "CURRENT POINTS: {:,}".format(rounded_score)
        # Render the string into an image
        self.score_image = self.font.render(score_str, True, self.settings.text_color, self.settings.background_color)

        # Align the image in the top right part of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    
    def prep_high_score(self):
        """ Converts a high score to an image """
        # Rounded the integer
        rounded_high_score = round(self.stats.high_score)
        # Forming a string
        high_score_str = "BEST RESULT: {:,}".format(rounded_high_score)
        # Render the string into an image
        self.high_score_image = self.font.render(high_score_str, True, self.settings.text_color, self.settings.background_color)

        # Align the image in the top center part of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 20
    

    def prep_lvl(self):
        """ Converts a lvl info to an image """
        # Forming string
        lvl_str = "LEVEL: " + str(self.stats.lvl)
        # Render the string into an image
        self.lvl_image = self.font.render(lvl_str, True, self.settings.text_color, self.settings.background_color)

        # Align the image under the current scoring
        self.lvl_rect = self.lvl_image.get_rect()
        self.lvl_rect.right = self.score_rect.right
        self.lvl_rect.top = self.score_rect.bottom + 10


    def prep_health(self):
        """ Convert health into a group of images """
        self.healths = Group()

        for health_number in range(self.stats.ships_left):
            health = Health()
            health.rect.x = 20 + health_number * (health.rect.width + 5)
            health.rect.y = 20
            self.healths.add(health)


    def show_score(self):
        """ Draws score board """
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.lvl_image, self.lvl_rect)
        self.healths.draw(self.screen)


    def check_high_score(self):
        """ Compares the current score with the highest and sets the new value in the highest """
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
