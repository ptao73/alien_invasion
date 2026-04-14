import sys
import pygame
from random import randint

from pygame.sprite import Sprite

class Star(Sprite):
    def __init__(self,sky_game):
        super().__init__()
        self.screen = sky_game.screen
        self.screen_rect = sky_game.screen.get_rect()
        self.image = pygame.Surface((5,5))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def update(self):
        """让星星随机闪烁"""
        # randint(0, 20) == 1 意味着每一帧都有 1/20 的概率改变透明度
        # 这样星星闪烁起来会更自然，而不是疯狂乱跳
        if randint(0, 20) == 1:
            # set_alpha 设置透明度：0 是完全透明（看控制不到），255 是完全不透明
            self.image.set_alpha(randint(50, 255))

            self.image_color = (randint(0, 255), randint(0, 255), randint(0, 255))
            self.image.fill(self.image_color)
            

            self.rect.y = randint(0, 800)
            self.rect.x = randint(0, 1200)



   
class Sky:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))
        self.stars = pygame.sprite.Group()
        pygame.display.set_caption("stars")

       
        for _ in range(50):
            new_star = Star(self)
            # 随机设置星星的位置
            new_star.rect.x = randint(0, 1200)
            new_star.rect.y = randint(0, 800)
            self.stars.add(new_star)


    
            
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.stars.update()
            self.screen.fill((0,0,0))
            self.stars.draw(self.screen)
            pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game.
    sky = Sky()
    sky.run_game()

        
        










