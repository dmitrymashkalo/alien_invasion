import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """ A class representing an alien """

    def __init__(self, ai_game):
        """ Init an alien and set initial position """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Upload the alien image
        self.image = pygame.image.load('images/alien_yellow.png')
        self.rect = self.image.get_rect()

        # Every new alien appear in left top corner of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Save position
        self.x = float(self.rect.x)


    def update(self):
        """ Moves the alien left or right """
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x


    def check_edges(self):
        """ Check edge of the screen """
        screen_rect = self.screen.get_rect()

        # Return True if an alien touch the edge of the screen
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
