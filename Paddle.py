"""@file Paddle

This module contains the Paddle class for the Pong game.
"""

import pygame
import constants

class Paddle:
    def __init__(self, pos_x: int, pos_y: int, width: int, height: int):
        self.posx = pos_x
        self.posy = pos_y
        self.width = width
        self.height = height

    def update(self, cursor_x: int):
        if cursor_x < 0:
            self.posx = 0
        elif cursor_x > constants.WINDOW_WIDTH - self.width:
            self.posx = constants.WINDOW_WIDTH - self.width
        else:
            self.posx = cursor_x
        
    def display(self, window: pygame.Surface):
        pygame.draw.rect(
            window,
            constants.WHITE,
            (self.posx, self.posy, self.width, self.height),
        )
