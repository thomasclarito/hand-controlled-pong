"""@file Paddle.py

This module contains the Paddle class for the Pong game.
"""

import pygame
from . import constants


class Paddle:
    def __init__(self, pos_x: int, pos_y: int, width: int, height: int):
        """The constructor for the Paddle class.

        Args:
            pos_x (int): the x-coordinate of the paddle
            pos_y (int): the y-coordinate of the paddle
            width (int): the width of the paddle
            height (int): the height of the paddle
        """
        self.posx = pos_x
        self.posy = pos_y
        self.width = width
        self.height = height

    def update(self, cursor_x: int):
        """Update the position of the paddle.

        Args:
            cursor_x (int): the x-coordinate of the cursor to update the paddle position
        """
        if cursor_x < 0:
            self.posx = 0
        elif cursor_x > constants.WINDOW_WIDTH - self.width:
            self.posx = constants.WINDOW_WIDTH - self.width
        else:
            self.posx = cursor_x

    def display(self, window: pygame.Surface):
        """Display the paddle on the game window.

        Args:
            window (pygame.Surface): the game window to display the paddle
        """
        pygame.draw.rect(
            window,
            constants.WHITE,
            (self.posx, self.posy, self.width, self.height),
        )
