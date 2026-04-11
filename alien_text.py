import sys

import pygame

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        # 设置背景色
        self.bg_color = (34, 65, 87)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.bg_color = (255,0,0)
                    elif event.key == pygame.K_UP:
                        self.bg_color = (0,255,0)
                    elif event.key == pygame.K_DOWN:
                        self.bg_color = (0,0,255)
                    elif event.key == pygame.K_RIGHT:
                        self.bg_color = (100,100,100)
                    else:
                        self.bg_color = (34, 65, 87)
                
            # 每次循环时都重绘屏幕
            self.screen.fill(self.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == "__main__":
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
