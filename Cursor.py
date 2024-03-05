"""@file Cursor.py

This module contains the Cursor class for navigating and interacting with the game.
"""

import pygame
from constants import RED


class Cursor:
    """@class Cursor

    Represents the cursor for navigating and interacting with the game.
    """

    def __init__(self):
        """Constructor for the Cursor class.
        Initializes the hand detector and the cursor position."""
        self.posx = -1
        self.posy = -1

    def display(self, window: pygame.Surface):
        """Draw the cursor on the screen."""
        pygame.draw.rect(window, RED, (self.posx + 9 , self.posy, 2, 20))
        pygame.draw.rect(window, RED, (self.posx, self.posy + 9 , 20, 2))

    def cleanup(self):
        """Cleanup the resources used by the cursor."""
        self.__hand_detector.cleanup()
