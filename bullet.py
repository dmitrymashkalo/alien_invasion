import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ Class for control bullet """

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.image = pygame.image.load('images/bullet.png')
        self.image = pygame.transform.scale(self.image, (self.settings.bullet_width, self.settings.bullet_height))


        # Create a bullet in position (0,0) and assign correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)