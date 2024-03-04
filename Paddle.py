"""@package Paddle

This module contains the Paddle class for the Pong game.
"""

import pygame


class Paddle:
    def __init__(self, pos_x: int, pos_y: int, width: int, height: int, speed: int):
        self.posx = pos_x
        self.posy = pos_y
        self.width = width
        self.height = height
        self.__speed = speed

    def move_left(self):
        self.posx -= self.__speed

    def move_right(self):
        self.posx += self.__speed

    def display(self, window: pygame.Surface):
        pygame.draw.rect(
            window,
            (255, 255, 255),
            (self.posx, self.posy, self.width, self.height),
        )
