import time
import math

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
        """updates player checks boundaries"""
        if self.rect.y <0:
            self.rect.y = 0
        elif self.rect.y > DISPLAY_HEIGHT - self.height:
            self.rect.y = DISPLAY_HEIGHT - self.height


    
    def move_up(self):
        """moves player up"""
        self.rect.y -= 15

    def move_down(self):
        """moves player down"""
        self.rect.y += 15

   

class Ball(pygame.sprite.Sprite):
    """class for pong ball object"""
    def __init__(self):
        super().__init__()

        self.side_length = 10
        self.color = WHITE
        self.image = pygame.Surface([self.side_length, self.side_length])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()


        self.rect.x = int(DISPLAY_WIDTH * 0.5 - (self.side_length * 0.5))
        self.rect.y = int(DISPLAY_HEIGHT * 0.5 - (self.side_length * 0.5))


        self.max_bounce_angle = 70
        self.x_velocity = 8.0
        self.y_velocity = 8.0

    def update(self):
        """updates rectangle position with the velocities"""
        self.rect.x = self.x_velocity
        self.rect.y = self.y_velocity


    def wall_bounce(self):
        """checks for bounce condition and calculates new velocities"""
        if self.rect.y <=0 or self.rect.y >= (DISPLAY_HEIGHT - self.side_length):
            self.y_velocity *= -1

    def player_bounce(self, player, player_designation):
        """calculates ball velocities for player bounce"""
        ball_speed = 11
        intersect_y = player.rect.y + (player.side_length / 2) - self.rect.y + (self.side_length / 2)
        normalized_intersect_y = math.fabs((intersect_y / player.height /2))
        bounce_angle = normalized_intersect_y * self.max_bounce_angle

        if player_designation == "P1":
            self.x_velocity = ball_speed * math.fabs(math.cos(bounce_angle))
            self.y_velocity = ball_speed * math.sin(bounce_angle)

        elif player_designation == "P2":
            self.x_velocity = ball_speed * math.fabs(math.cos(bounce_angle)) * -1
            self.y_velocity = ball_speed * math.sin(bounce_angle)




def quit_game():
    """quits the game and pygame"""
    pygame.quit()
    quit()

ball = Ball()

pong_balls = pygame.sprite.Group()
pong_balls.add(ball)

player_one = Player(DISPLAY_WIDTH * 0.1)
player_two = Player(DISPLAY_WIDTH * 0.9)

pong_players = pygame.sprite.Group()
pong_players.add(player_one)
pong_players.add(player_two)

def game_loop():
    """executes game loop and game logic"""
    game_exit = False
    while game_exit != True:

        pygame.display.update()
        CLOCK.tick(FPS)

game_loop()