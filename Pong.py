"""@package Pong

This module contains the Pong class for the Pong game.
"""

import random
from enum import Enum

# Import the Ball and Paddle classes
import constants
from Ball import Ball
from Paddle import Paddle


# Paddle parameters
paddle_width = 80
paddle_height = 10
paddle_speed = 8

init_paddle_x = constants.WINDOW_WIDTH // 2 - paddle_width // 2
init_paddle_y = constants.WINDOW_HEIGHT - paddle_height - 20

# Ball parameters
ball_radius = 10
init_ball_speed_x = random.choice([-3, 3])
init_ball_speed_y = 3
init_ball_x = constants.WINDOW_WIDTH // 2
init_ball_y = constants.WINDOW_HEIGHT // 2


class Pong:
    def __init__(self):
        self.ball = Ball(
            init_ball_x, init_ball_y, ball_radius, init_ball_speed_x, init_ball_speed_y
        )
        self.player_paddle = Paddle(
            init_paddle_x, init_paddle_y, paddle_width, paddle_height, paddle_speed
        )

    def reset(self):
        self.ball = Ball(
            init_ball_x, init_ball_y, ball_radius, init_ball_speed_x, init_ball_speed_y
        )
        self.player_paddle = Paddle(
            init_paddle_x, init_paddle_y, paddle_width, paddle_height, paddle_speed
        )
