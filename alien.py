import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load image alien and assign attribute rect
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        # Every new alien appear in left top corner of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Save position
        self.x = float(self.rect.x)


    def update(self):
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x


    def check_edges(self):
        """ Return True if an alien in the edge of the screen """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True