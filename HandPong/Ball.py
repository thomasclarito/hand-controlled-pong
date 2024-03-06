"""@file Ball.py

This module contains the Ball class for the Pong game.
"""

import pygame

# Import the Paddle class
from . import constants
from .Paddle import Paddle


# Ball class for the pong game
#
class Ball:
    def __init__(
        self, pos_x: int, pos_y: int, radius: int, speed_x: int, speed_y: int
    ):
        """The constructor for the Ball class.

        Args:
            pos_x (int): the x-coordinate of the ball in the window, as pixels
            pos_y (int): the y-coordinate of the ball in the window, as pixels
            radius (int): the radius of the ball, as pixels
            speed_x (int): the speed of the ball in the x-direction
            speed_y (int): the speed of the ball in the y-direction
        """
        self.__posx = pos_x
        self.__posy = pos_y
        self.__radius = radius
        self.__speedx = speed_x
        self.__speedy = speed_y
        self.hit_count = 0

    def move(self):
        """Move the ball in the window."""
        self.__posx += self.__speedx
        self.__posy += self.__speedy

    def display(self, window: pygame.Surface):
        """Draw the ball on the screen.
        
        Args:
            window (pygame.Surface): the game window to display the ball
        """
        pygame.draw.circle(
            window, constants.WHITE, (self.__posx, self.__posy), self.__radius
        )

    def check_collision(self, paddle: Paddle) -> bool:
        """Check for collision of the ball with the paddle and the walls.

        Args:
            paddle (Paddle): the paddle object, to check for collision with the ball

        Returns:
            bool: True if the ball is still in play, False if the ball is out of play
        """
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
        if (
            self.__posx <= 0
            or self.__posx >= constants.WINDOW_WIDTH - self.__radius
        ):
            self.__speedx = -self.__speedx
        # check collision with the top wall
        if self.__posy <= 0:
            self.__speedy = -self.__speedy

        # check collision with the bottom wall
        if self.__posy >= constants.WINDOW_HEIGHT - self.__radius:
            return False

        return True
