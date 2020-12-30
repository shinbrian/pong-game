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
    def __init__(self, x_position):
        super().__init__()

        self.width = 15
        self.height = 90

        self.y_velocity = 0

        self.color = WHITE

        self.image = pygame.Surface(self.width, self.height)
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()

        self.rect.x = x_position
        self.y_position = (DISPLAY_HEIGHT // 2) - 10
        self.rect.y = self.y_position() + 0