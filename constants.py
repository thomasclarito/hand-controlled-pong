""" constants.py
This module contains constants for the game.
"""
from enum import Enum

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


class GameState(Enum):
    INTRO = 1
    PLAY = 2
    GAME_OVER = 3
