import sys
import pygame

class AlienInvasion:
    """A class for managing resources and game behavior."""

    def __init__(self):
        """Initiates the game and creates game resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        # Set up background color.
        self.background_color = (230, 230, 230)
        
    def run_game(self):
        """The main game loop."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Fill screen with to background color.
            self.screen.fill(self.background_color)

            # Update screen
            pygame.display.flip()


if __name__ == '__main__':
    # Create an object and run the game.
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()