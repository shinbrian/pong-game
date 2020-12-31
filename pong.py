import time

import pygame

pygame.init()

DISPLAY_WIDTH = 950
DISPLAY_HEIGHT = 570

FPS = 60

CLOCK = pygame.time.Clock()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

GAME_DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

def game_loop():
    """execute game loop and game logic"""
    game_exit = False
    while game_exit != True:

        pygame.display.update()
        CLOCK.tick(FPS)

game_loop()