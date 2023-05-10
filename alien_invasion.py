import sys
import pygame
from time import sleep
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button


class AlienInvasion:
    """ A class for managing resources and game behavior """

    def __init__(self):
        """ Initiates the game and creates game resources """
        pygame.init()
        self.settings = Settings()

        if self.settings.full_screen_mode: # Full screen mode
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else: # Window mode
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        # Name
        pygame.display.set_caption(self.settings.screen_name)

        # Background
        self.bg = pygame.image.load('images/background.jpg')
        self.bg = pygame.transform.scale(self.bg, (self.settings.screen_width, self.settings.screen_height))

        # Create an object for store game stats
        self.stats = GameStats(self)


        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.button = Button(self, 'Start')

        self._create_fleet()

        
    def run_game(self):
        """The main game loop."""
        while True:
            self._check_events()

            if self.stats.game_active:
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

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)


    def _check_play_button(self, mouse_pos):
        """ Starts new game after clicking on the button """

        if self.button.rect.collidepoint(mouse_pos) and not self.stats.game_active:
            # Reset game stats
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True

            # Clear list of aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and move the ship in the center
            self._create_fleet()
            self.ship.center_ship()

            pygame.mouse.set_visible(False)


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
        elif event.key == pygame.K_0:
            self.settings.increase_speed()


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

        self._check__bullet_alien_collisions()


    def _check__bullet_alien_collisions(self):
        """ Check for alien hits """
        # When a hit is detected, remove the bullet and the alien - True, True.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        # Create new fleet if old is empty
        if not self.aliens:
            # Delete existing bullets
            self.bullets.empty()
            self.settings.increase_speed()
            self._create_fleet()


    def _check_aliens_bottom(self):
        """ Checks if the aliens have reached the bottom of the screen """
        screen_rect = self.screen.get_rect()

        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break
    

    def _ship_hit(self):
        # Increase ships left
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1

            # Clear list of aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and move the ship in the center
            self._create_fleet()
            self.ship.center_ship()

            # Pause the game
            sleep(0.5)
        else:
            self.stats.game_active = False



    def _update_aliens(self):
        self._check_fleet_edges()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Checks if the aliens have reached the bottom
        self._check_aliens_bottom()

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
        # Fill screen with to background color or background image.
        #self.screen.fill(self.settings.background_color)
        self.screen.blit(self.bg, (0, 0))

        # Ship
        self.ship.blitme()

        # Bullet
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Aliens
        self.aliens.draw(self.screen)

        # Play button
        if not self.stats.game_active:
            self.button.draw_button()

        # Update screen
        pygame.display.flip()
         

if __name__ == '__main__':
    # Create an object and run the game
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()