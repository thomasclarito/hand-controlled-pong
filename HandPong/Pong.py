"""@file Pong.py

This module contains the Pong class for the Pong game.
"""

import pickle
import random
from enum import Enum

# Import the constants module, Ball, and Paddle classes
from . import constants
from .Ball import Ball
from .Paddle import Paddle


# Paddle parameters
paddle_width = 80
paddle_height = 10

init_paddle_x = constants.WINDOW_WIDTH // 2 - paddle_width // 2
init_paddle_y = constants.WINDOW_HEIGHT - paddle_height - 20

# Ball parameters
ball_radius = 10
init_ball_speed_x = random.choice([-5, 5])
init_ball_speed_y = 5
init_ball_x = constants.WINDOW_WIDTH // 2
init_ball_y = constants.WINDOW_HEIGHT // 2


class Pong:
    def __init__(self):
        """The constructor for the Pong class"""
        self.ball = Ball(
            init_ball_x,
            init_ball_y,
            ball_radius,
            init_ball_speed_x,
            init_ball_speed_y,
        )
        self.player_paddle = Paddle(
            init_paddle_x, init_paddle_y, paddle_width, paddle_height
        )
        try:
            with open("./score.dat", "rb") as file:
                self.hiscore = pickle.load(file)
        except:
            pass
        finally:
            self.hiscore = 0

    def update_hiscore(self):
        """Update the hiscore of the Pong game."""
        self.hiscore = max(self.hiscore, self.ball.hit_count)
        with open("./score.dat", "wb") as file:
            pickle.dump(self.hiscore, file)

    def reset(self):
        """Reset the ball and paaddle to their initial positions."""
        self.ball = Ball(
            init_ball_x,
            init_ball_y,
            ball_radius,
            init_ball_speed_x,
            init_ball_speed_y,
        )
        self.player_paddle = Paddle(
            init_paddle_x, init_paddle_y, paddle_width, paddle_height
        )
