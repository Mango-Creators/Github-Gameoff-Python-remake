import pygame


class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, image, center_coords, velocity):
        super().__init__()
        self.base_image = image
        self.image = self.base_image
        self.rect = self.image.get_rect(center=center_coords)
        self.velocity = velocity
        self.keys_pressed = pygame.key.get_pressed()
        self.scaling_factor = 1.0
        self.clock = pygame.time.Clock()
        self.delta_time = self.clock.tick(60)/1000
    def move(self):

        if self.keys_pressed[pygame.K_w]:
            self.rect.centery -= self.velocity * self.delta_time
        if self.keys_pressed[pygame.K_s]:
            self.rect.centery += self.velocity * self.delta_time

    def scale(self):
        # Store the old center of the rectangle
        old_center = self.rect.center

        # Adjust the scaling factor based on a key press
        if self.keys_pressed[pygame.K_a]:
            self.scaling_factor += 0.05  # Increase scaling factor when SPACE key is pressed
            if self.scaling_factor > 6.0:
                self.scaling_factor = 6.0  # Limit the maximum scaling factor
        if self.keys_pressed[pygame.K_d]:
            self.scaling_factor -= 0.05
            if self.scaling_factor < 0.01:
                self.scaling_factor = 0.01

        # Scale the image based on the scaling factor
        new_width = int(self.base_image.get_width() * self.scaling_factor)
        new_height = int(self.base_image.get_height() * self.scaling_factor)
        self.image = pygame.transform.scale(self.base_image, (new_width, new_height))

        # Update the rectangle with the new size
        self.rect = self.image.get_rect(center=old_center)

    def update(self):
        self.delta_time = self.clock.tick(60) / 1000
        self.keys_pressed = pygame.key.get_pressed()
        self.move()
        self.scale()
