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

class Player(pygame.sprite.Sprite):
    """player class for player object"""
    def __init__(self, x_position):
        self.width = 15
        self.height = 90

        self.color = WHITE
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        self.rect.x = x_position
        self.rect.y = (DISPLAY_HEIGHT // 2) - self.height // 2

def game_loop():
    """execute game loop and game logic"""
    game_exit = False
    while game_exit != True:

        pygame.display.update()
        CLOCK.tick(FPS)

game_loop()