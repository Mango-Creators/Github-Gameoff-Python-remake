import pygame
pygame.init()

# Events
GAME_OVER_EVENT = pygame.USEREVENT + 1
RESTART_EVENT = pygame.USEREVENT + 2
SCORE_INCREMENT_EVENT = pygame.USEREVENT + 3