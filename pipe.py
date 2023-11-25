import pygame

import random


class PipePair(pygame.sprite.Sprite):
    def __init__(self, screen: pygame.Surface):
        super().__init__()
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.delta_time = self.clock.tick(60) / 1000
        self.upper_pipe = pygame.rect.Rect(0, 0, 50, self.screen.get_height())
        self.lower_pipe = pygame.rect.Rect(0, 0, 50, self.screen.get_height())
        self.set_upper_rect()
        while True:
            try:
                self.gap = random.randint(25, (self.screen.get_height() - self.upper_pipe.bottomleft[1]) + 10)
            except:
                self.set_upper_rect()
                self.gap = random.randint(25, (self.screen.get_height() - self.upper_pipe.bottomleft[1]) + 10)
                continue
            break
        self.set_lower_rect()


    def set_upper_rect(self):
        x_pos = self.screen.get_width() + 10
        y_pos = random.randint(0, self.screen.get_width() // 2)
        self.upper_pipe.bottomleft = (x_pos, y_pos)

    def set_lower_rect(self):
        x_pos = self.screen.get_width() + 10
        y_pos = self.upper_pipe.bottomleft[1] + self.gap

        self.lower_pipe.topleft = (x_pos, y_pos)

    def move(self):
        self.upper_pipe.x -= 100 * self.delta_time
        self.lower_pipe.x -= 100 * self.delta_time

    def update(self):
        self.delta_time = self.clock.tick(60) / 1000
        self.move()
        pygame.draw.rect(self.screen, (255, 255, 255), self.upper_pipe)
        pygame.draw.rect(self.screen, (255, 255, 255), self.lower_pipe)


"""
1. Flip around make a copy and sprite group and all that
2. set a gap between them (random, but leans towards smaller sizes)
3. set motion to them
4. check for collison with space ship
5. check if the space ship size is big or small enough
6. send out a signal
"""
