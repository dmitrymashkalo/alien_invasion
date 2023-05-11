import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard:
    """ Class for displaing game info """

    def __init__(self, ai_game):
        """ Init scoring attributes """
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Text properties
        self.text_color = (60, 60, 60)
        self.bg_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        # Prepering image
        self.prep_score()
        self.prep_high_score()
        self.prep_lvl()
        self.prep_health()

    
    def prep_score(self):
        """ Converts the current score to an image """
        rounded_score = round(self.stats.score)
        score_str = "CURRENT POINTS: {:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.bg_color)

        # Вывод счета в правой верхней части экрана.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    
    def prep_high_score(self):
        """ Converts a high score to an image """
        rounded_high_score = round(self.stats.high_score)
        high_score_str = "BEST RESULT: {:,}".format(rounded_high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.bg_color)

        # Вывод счета в центральной верхней части экрана
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 20
    

    def prep_lvl(self):
        """ Converts a lvl info to an image"""
        lvl_str = "LEVEL: " + str(self.stats.lvl)
        self.lvl_image = self.font.render(lvl_str, True, self.text_color, self.bg_color)

        self.lvl_rect = self.lvl_image.get_rect()
        self.lvl_rect.right = self.score_rect.right
        self.lvl_rect.top = self.score_rect.bottom + 10


    def prep_health(self):
        self.health = Group()

        for health in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 20 + health * (ship.rect.width + 5)
            ship.rect.y = 10
            self.health.add(ship)


    def show_score(self):
        """ Draw score board """
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.lvl_image, self.lvl_rect)
        self.health.draw(self.screen)


    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
