import pygame
import random

from space_ship import SpaceShip


class PipePair(pygame.sprite.Sprite):
    def __init__(self, screen: pygame.Surface, player):
        super().__init__()
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.delta_time = self.clock.tick(60) / 1000
        self.upper_pipe = pygame.rect.Rect(0, 0, 50, self.screen.get_height())
        self.lower_pipe = pygame.rect.Rect(0, 0, 50, self.screen.get_height())
        self.collider = pygame.rect.Rect(0, 0, 0, 0)
        self.required_scales_to_pass_pipes = []
        self.set_upper_rect()
        self.player = player
        while True:
            try:
                self.gap = random.randint(25, (self.screen.get_height() - self.upper_pipe.bottomleft[1]) + 10)
            except:
                self.set_upper_rect()
                self.gap = random.randint(25, (self.screen.get_height() - self.upper_pipe.bottomleft[1]) + 10)
                continue
            break
        self.set_lower_rect()
        self.set_invisible_collider()
        self.calculate_scale_to_pass_pipes()


    def set_upper_rect(self):
        x_pos = self.screen.get_width() + 10
        y_pos = random.randint(0, self.screen.get_width() // 2)
        self.upper_pipe.bottomleft = (x_pos, y_pos)

    def set_lower_rect(self):
        x_pos = self.screen.get_width() + 10
        y_pos = self.upper_pipe.bottomleft[1] + self.gap

        self.lower_pipe.topleft = (x_pos, y_pos)
    
    # Start of invisible game objects
    def set_invisible_collider(self):
        self.collider.topright = self.upper_pipe.bottomright
        self.collider.width = 10
        self.collider.height = self.gap    
    
    def update_invisible_collider(self):
        self.collider.topright = self.upper_pipe.bottomright
    
    def move(self):
        self.upper_pipe.x -= 100 * self.delta_time # type: ignore
        self.lower_pipe.x -= 100 * self.delta_time # type: ignore

    def update(self):
        self.delta_time = self.clock.tick(60) / 1000
        self.check_player_status(self.player)
        self.move()
        # self.set_invisible_collider()
        self.update_invisible_collider()
        pygame.draw.rect(self.screen, (255, 255, 255), self.upper_pipe)
        pygame.draw.rect(self.screen, (255, 255, 255), self.lower_pipe)
        pygame.draw.rect(self.screen, (255, 0, 0), self.collider)
    
    def check_player_status(self, player: SpaceShip):
        
        if self.collider.colliderect(player.rect):
            if not (self.required_scales_to_pass_pipes[0] <= player.scaling_factor <= self.required_scales_to_pass_pipes[1]):
                return True
            else:
                 return False
        else:
            return False
    
    def calculate_scale_to_pass_pipes(self):
        # 1/96, 6/576
        # height is betweeen (gap-20, gap-1)
        height_range = (self.gap/2, self.gap - 1)
        scale = []
        scale.append(height_range[0]/96)
        scale.append(height_range[1]/96)
        self.required_scales_to_pass_pipes = scale
        
        


"""
1. Flip around make a copy and sprite group and all that
2. set a gap between them (random, but leans towards smaller sizes)
3. set motion to them
4. check for collison with space ship
5. check if the space ship size is big or small enough
6. send out a signal
"""
