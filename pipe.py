import pygame
import random
from events import GAME_OVER_EVENT

from space_ship import SpaceShip

class PipePair(pygame.sprite.Sprite):
    def __init__(self, screen: pygame.Surface, player: SpaceShip):
        super().__init__()
        self.collider = pygame.rect.Rect(0, 0, 0, 0)
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.delta_time = self.clock.tick(60) / 1000
        self.upper_pipe = pygame.rect.Rect(0, 0, 50, self.screen.get_height())
        self.lower_pipe = pygame.rect.Rect(0, 0, 50, self.screen.get_height())
        self.gap = 0
        self.player = player
        self.height_range = []
        self.set_upper_rect()
        self.set_gap()
        self.set_lower_rect()
        self.set_collider()
        self.set_height_range()

    # Initial Pipe Settings
    def set_upper_rect(self):
        x_pos = self.screen.get_width() + 10
        y_pos = random.randint(0, self.screen.get_height() // 2)
        self.upper_pipe.bottomleft = (x_pos, y_pos)
        
    def set_lower_rect(self):
        x_pos = self.screen.get_width() + 10
        y_pos = self.upper_pipe.bottomleft[1] + self.gap
        
        self.lower_pipe.topleft = (x_pos, y_pos)
        
    def set_gap(self):
        self.gap = random.randint(self.upper_pipe.bottomleft[1], self.screen.get_height()+10)
    
    # Collider Stuff
    def set_collider(self):
        pos = self.upper_pipe.bottomright
        height = self.gap
        
        self.collider.topright = pos
        self.collider.width = 15
        self.collider.height = height
    
    def update_collider(self):
        self.collider.topright = self.upper_pipe.bottomright
    
    def set_height_range(self):
        self.height_range = [(3/5) * self.gap, self.gap]
    
    # Active gameplay
    def move(self):
        self.upper_pipe.x -= 100 * self.delta_time # type: ignore
        self.lower_pipe.x -= 100 * self.delta_time # type: ignore
        
    def update(self):
        self.delta_time = self.clock.tick(60) / 1000
        
        self.move()
        self.update_collider()
        self.check_for_collision()
        # self.set_invisible_collider()
        pygame.draw.rect(self.screen, (255, 255, 255), self.upper_pipe)
        pygame.draw.rect(self.screen, (255, 255, 255), self.lower_pipe)
        pygame.draw.rect(self.screen, (255, 0, 0), self.collider)
    
    def check_for_collision(self):
        if self.collider.colliderect(self.player):
            if not(self.height_range[0] <= self.player.rect.height <= self.height_range[1]):
                pygame.event.post(pygame.event.Event(GAME_OVER_EVENT))
        if self.upper_pipe.colliderect(self.player) or self.lower_pipe.colliderect(self.player):
            pygame.event.post(pygame.event.Event(GAME_OVER_EVENT))
    
    

"""
1. Flip around make a copy and sprite group and all that
2. set a gap between them (random, but leans towards smaller sizes)
3. set motion to them
4. check for collison with space ship
5. check if the space ship size is big or small enough
6. send out a signal
"""
