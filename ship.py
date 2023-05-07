import pygame

class Ship:

    def __init__(self, ai_game):
        """Init ship and set initial position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Upload the ship img
        self.img = pygame.image.load('images/ship.png')
        self.rect = self.img.get_rect()

        # Every new ship will appear on mid bottom
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        """Draw the ship"""
        self.screen.blit(self.img, self.rect)