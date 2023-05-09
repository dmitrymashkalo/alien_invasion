import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """A class for managing resources and game behavior."""

    def __init__(self):
        """Initiates the game and creates game resources."""
        pygame.init()
        self.settings = Settings()

        if self.settings.full_screen_mode == True:
            # Full screen mode
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else:
            # Window mode
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # Name
        pygame.display.set_caption(self.settings.name)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        
    def run_game(self):
        """The main game loop."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()


    def _check_events(self):
        """Events handle."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        """Events handle."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _check_keyup_events(self, event):
        """Events handle."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    
    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        # Check for alien hits.
        # When a hit is detected, remove the bullet and the alien - True, True.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)


    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

    
    def _create_fleet(self):
        """Creation of an invasion fleet"""
        
        alien = Alien(self)
        alien_width, alien_height = alien.rect.width, alien.rect.height
        available_space_x = self.settings.screen_width - (alien_width * 2)
        number_aliens_x = available_space_x // (alien_width * 2)

        # Определяем кол-во рядов помещающихся на экране
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (3 * alien_height) - ship_height
        number_rows = available_space_y // (alien_height * 2)

        # Create fleet
        for row in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row)


    def _create_alien(self, alien_number, row_number):
        """ Create an alien and place it into the row """
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)


    def _check_fleet_edges(self):
        """ Reacts when an alien reaches the edge of the screen. """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break


    def _change_fleet_direction(self):
        """ Lowers the entire fleet and reverses the direction of the fleet. """
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _update_screen(self):
            """Update the images on the screen and displays the new screen."""
            # Fill screen with to background color.
            self.screen.fill(self.settings.background_color)

            # Ship
            self.ship.blitme()

            # Bullet
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()

            # Aliens
            self.aliens.draw(self.screen)

            # Update screen
            pygame.display.flip()
         


if __name__ == '__main__':
    # Create an object and run the game.
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()