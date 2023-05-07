import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """A class for managing resources and game behavior."""

    def __init__(self):
        """Initiates the game and creates game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.name)

        self.ship = Ship(self)

        
    def run_game(self):
        """The main game loop."""
        while True:
            self._check_events()
            self._update_screen()


    def _check_events(self):
        """Events handle."""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


    def _update_screen(self):
            """Update the images on the screen and displays the new screen."""
            # Fill screen with to background color.
            self.screen.fill(self.settings.background_color)

            # Ship
            self.ship.blitme()

            # Update screen
            pygame.display.flip()
         


if __name__ == '__main__':
    # Create an object and run the game.
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()