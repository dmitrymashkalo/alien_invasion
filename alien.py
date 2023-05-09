import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        # Load image alien and assign attribute rect
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        # Every new alien appear in left top corner of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Save position
        self.x = float(self.rect.x)