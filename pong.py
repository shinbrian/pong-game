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
        super().__init__()
        self.width = 15
        self.height = 90

        self.color = WHITE
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        self.rect.x = int(x_position)
        self.rect.y = int((DISPLAY_HEIGHT // 2) - self.height // 2)


    def update(self):
        if self.rect.y <0:
            self.rect.y = 0
        elif self.rect.y > DISPLAY_HEIGHT - self.height:
            self.rect.y = DISPLAY_HEIGHT - self.height


    
    def move_up(self):
        """move player up"""
        self.rect.y -= 15

    def move_down(self):
        """move player down"""
        self.rect.y += 15

   

class Ball(pygame.sprite.Sprite):
    """class for pong ball object"""
    def __init__(self):
        super().__init__()

        self.side_length = 10
        self.color = WHITE
        self.image = pygame.Surface([self.side_length, self.side_length])
        self.image.fill(self.color)
        self.rect = self.image.get_rect


        self.rect.x = int(DISPLAY_WIDTH * 0.5 - (self.side_length * 0.5))
        self.rect.y = int(DISPLAY_HEIGHT * 0.5 - (self.side_length * 0.5))


        self.max_bounce_angle = 70
        self.x_velocity = 8.0
        self.y_velocity = 8.0

    def update(self):
        """updater rectangle position with the velocities"""
        self.rect.x = self.x_velocity
        self.rect.y = self.y_velocity




def quit_game():
    """quit the game and pygame"""
    pygame.quit()
    quit()


def game_loop():
    """execute game loop and game logic"""
    game_exit = False
    while game_exit != True:

        pygame.display.update()
        CLOCK.tick(FPS)

game_loop()