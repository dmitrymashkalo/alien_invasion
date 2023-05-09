import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """ Class for control ship's bullets"""

    def __init__(self, ai_game):
        """ Init bullet and set initial position """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Upload the bullet image and transform it
        self.image = pygame.image.load('images/bullet.png')
        self.image = pygame.transform.scale(self.image, (self.settings.bullet_width, self.settings.bullet_height))

        # Get rect a bullet and set its position
        self.rect = self.image.get_rect()
        self.rect.midtop = ai_game.ship.rect.midtop

        # Save coordinats of bullet in self.y as a float
        self.y = float(self.rect.y)


    def update(self):
        """ Moves the bullet up the screen """
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y


    def draw_bullet(self):
        """ Draw the bullet at the current position """
        self.screen.blit(self.image, self.rect)