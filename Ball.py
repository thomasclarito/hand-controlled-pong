"""@file Ball.py

This module contains the Ball class for the Pong game.
"""

import pygame
import random

# Import the Paddle class
import Paddle


## Ball class for the pong game
#
class Ball:
    def __init__(self, pos_x: int, pos_y: int, radius: int, speed_x: int, speed_y: int):
        self.__posx = pos_x
        self.__posy = pos_y
        self.__radius = radius
        self.__speedx = speed_x
        self.__speedy = speed_y
        self.hit_count = 0

    def move(self):
        self.__posx += self.__speedx
        self.__posy += self.__speedy

    def display(self, window: pygame.Surface):
        pygame.draw.circle(
            window, (255, 255, 255), (self.__posx, self.__posy), self.__radius
        )

    def check_collision(self, paddle: Paddle, window: pygame.Surface) -> bool:
        # check collision with the paddle
        if (
            self.__posy >= paddle.posy - self.__radius
            and paddle.posx <= self.__posx <= paddle.posx + paddle.width
        ):
            # track the number of hits
            self.hit_count += 1
            # increase the speed of the ball after every 2 hits
            self.__speedx += self.hit_count // 2
            self.__speedy += self.hit_count // 2

            # change the direction of the ball
            self.__speedy = -abs(self.__speedy)

        # check collision with the side walls
        if self.__posx <= 0 or self.__posx >= window.get_width() - self.__radius:
            self.__speedx = -self.__speedx
        # check collision with the top wall
        if self.__posy <= 0:
            self.__speedy = -self.__speedy

        # check collision with the bottom wall
        if self.__posy >= window.get_height() - self.__radius:
            return False

        return True
