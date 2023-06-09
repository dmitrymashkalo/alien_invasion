import pygame


class Ship():
    """ Ship control class"""

    def __init__(self, ai_game):
        """ Init ship and set initial position """
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Upload the ship img
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

        # Align ship on mid bottom
        self.rect.midbottom = self.screen_rect.midbottom

        # Save coordinats of ship in self.x as a float
        self.x = float(self.rect.x)

        # Moving flags
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """ Updates the ship's position based on the flag """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x


    def blitme(self):
        """ Draw the ship at the current position """
        self.screen.blit(self.image, self.rect)


    def center_ship(self):
        """ Move the ship in the mid bottom """
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)