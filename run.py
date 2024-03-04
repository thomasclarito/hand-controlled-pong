"""@file run.py

This module contains the main function for the Pong game.
"""

import pygame
from enum import Enum

# Import the Pong and PongManager classes
from PongManager import PongManager
from Pong import Pong


def main():
    pong = Pong()
    gm = PongManager(pong)
    gm.run()


if __name__ == "__main__":
    main()
    pygame.quit()
