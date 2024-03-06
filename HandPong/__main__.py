"""@file run.py

This module contains the main function for the Pong game.
"""

import pygame
from enum import Enum

# Import the Pong and PongManager classes
from HandPong.PongManager import PongManager
from HandPong.Pong import Pong


def main():
    """Run the Pong game."""
    pong = Pong()
    gm = PongManager(pong)
    gm.run()


if __name__ == "__main__":
    main()
    pygame.quit()
