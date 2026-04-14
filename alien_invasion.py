import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien



class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
            self.clock.tick(60)
            
    def _check_events(self):    
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        """self._hello_world(event)"""

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    """def _hello_world(self, event):
        if event.key == pygame.K_h:
            print("Hello World")
        elif event.key == pygame.K_f:
            print("Fighting!")
        elif event.key == pygame.K_g:
            print("You are a good guy!")"""

    def _update_bullets(self):

        """Update position of bullets."""
        self.bullets.update()

        # Remove bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        """Check for collisions between bullets and aliens."""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        #available_space_x = self.settings.screen_width - (2 * alien_width)
        #number_aliens_x = available_space_x // (2 * alien_width)
        curent_x, curent_y = alien_width, alien_height

        while curent_y < self.screen_height - 3 * alien_height - self.ship.rect.height:
            while curent_x < self.screen_width - 2 * alien_width:
                self._create_alien(curent_x, curent_y)
                curent_x += 2 * alien_width
                
            curent_x = alien_width
            curent_y += 2 * alien_height

        print(f"目前群组里有 {len(self.aliens)} 个外星人") # 加这一行
        print(f"DEBUG: 屏幕宽={self.screen_width}, 高={self.screen_height}, 外星人宽={alien_width}, 飞船高={self.ship.rect.height}")

        
        # Determine the number of rows of aliens that fit on the screen.
        # ship_height = self.ship.rect.height
        # available_space_y = (self.settings.screen_height -
        #                        (3 * alien_height) - ship_height)
        # number_rows = available_space_y // (2 * alien_height)
        
        # Create the full fleet of aliens.
        #    for row_number in range(number_rows):
            # for alien_number in range(number_aliens_x):
                # self._create_alien(alien_number, row_number)

    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the row."""
        new_alien = Alien(self)
        alien_width, alien_height = new_alien.rect.size
        new_alien.x = x_position
        new_alien.y = y_position
        new_alien.rect.x = new_alien.x
        new_alien.rect.y = new_alien.y
        self.aliens.add(new_alien)


        
    def _check_fleet_edges(self):
        """Check if any aliens have reached the edge of the screen."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Change the direction of the fleet."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()


    def _update_screen(self):
            """Update images on the screen, and flip to the new screen."""
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()

            self.aliens.draw(self.screen)
    
            # Make the most recently drawn screen visible.
            pygame.display.flip()
           

if __name__ == "__main__":
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()