import pygame

import space_ship
pygame.init()
d = space_ship.SpaceShip(pygame.image.load("Main Ship - Base - Damaged.png"), (50, 50), 500)

print(type(d))