"""@file PongManager.py

This module contains the PongManager class for the Pong game.
"""

import pygame

import constants
from constants import GameState
from Ball import Ball
from Paddle import Paddle
from Pong import Pong
from HandDetector import HandDetector


class PongManager:
    """@class PongManager 
      
    Manages the game loop and the game states."""

    def __init__(self, pong: Pong):
        """Constructor for the PongManager class.
        Initialized pygame, font, the game window, and the game clock."""
        pygame.init()
        pygame.display.set_caption("Pong")
        pygame.font.init()
        self.__window = pygame.display.set_mode(
            (constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT)
        )
        self.__clock = pygame.time.Clock()
        self.__is_running = True
        self.__current_state = GameState.INTRO
        self.__font = pygame.font.SysFont("consolas", 30)
        self.__pong = pong
        self.__hand_detector = HandDetector()

    def run(self):
        """Run the game loop.
        There are game loop contains 3 states: intro, play, and game over.
        The intro displays the game title and a prompt to start the game.
        The play state contains the main game loop.
        The game over state displays the game over message and a prompt to restart the game.
        """

        while self.__is_running:
            if self.__current_state == GameState.INTRO:
                self.handle_intro_state()
            elif self.__current_state == GameState.PLAY:
                self.handle_play_state()
            elif self.__current_state == GameState.GAME_OVER:
                self.handle_gameover_state()

            # Update the display
            pygame.display.flip()
            # Limit the frame rate
            self.__clock.tick(60)

        self.cleanup()

    def handle_intro_state(self):
        """Handle the intro state events.
        Updates the current state to play when the space key is pressed.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__is_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.__current_state = GameState.PLAY

        self.draw_intro()

    def handle_play_state(self):
        """Handle the play state events.
        Updates the current state to game over when the ball hits the bottom wall.

        The player's paddle is moved based on the left and right arrow keys.
        THe ball is moved and checked for collision with the player's paddle.

        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__is_running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.__pong.player_paddle.posx > 0:
            self.__pong.player_paddle.move_left()
        if (
            keys[pygame.K_RIGHT]
            and self.__pong.player_paddle.posx
            < constants.WINDOW_WIDTH - self.__pong.player_paddle.width
        ):
            self.__pong.player_paddle.move_right()

        self.__pong.ball.move()
        if not self.__pong.ball.check_collision(
            self.__pong.player_paddle, self.__window
        ):
            self.__current_state = GameState.GAME_OVER
            return
        self.__window.fill(constants.BLACK)

        self.draw_play()

    def handle_gameover_state(self):
        """Handle the game over state events.
        Updates the current state to play when the space key is pressed.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__is_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.__pong.reset()
                    self.__current_state = GameState.PLAY

        self.draw_gameover()

    def draw_intro(self):
        """Display the intro screen.
        Draw "Pong" and "Press Space to Play" in the center of the screen.
        """
        intro_text = self.__font.render("Pong", True, constants.WHITE)
        press_space_text = self.__font.render(
            "Press Space to Play", True, constants.WHITE
        )
        self.__window.fill(constants.BLACK)
        self.__window.blit(
            intro_text,
            (
                (constants.WINDOW_WIDTH - intro_text.get_width()) // 2,
                constants.WINDOW_HEIGHT // 2 - intro_text.get_height() - 10,
            ),
        )
        self.__window.blit(
            press_space_text,
            (
                (constants.WINDOW_WIDTH - press_space_text.get_width()) // 2,
                constants.WINDOW_HEIGHT // 2,
            ),
        )

    def draw_play(self):
        """Display the game screen.
        Draw the player's paddle, the ball, and the score.
        """
        self.__pong.player_paddle.display(self.__window)
        self.__pong.ball.display(self.__window)
        cursor = self.__hand_detector.get_pointer_location()
        if cursor:
            pygame.draw.rect(self.__window, constants.RED, (cursor[0], cursor[1], 2, 2))
            self.__pong.player_paddle.update(cursor)
        score = self.__font.render(
            f"Score: {self.__pong.ball.hit_count}", True, constants.WHITE
        )
        self.__window.blit(score, (10, 10))

    def draw_gameover(self):
        """Display the game over screen.
        Draw "Game Over" and "Press Space to play again" in the center of the screen.
        """
        gameover_text = self.__font.render("Game Over", True, constants.WHITE)
        score_text = self.__font.render(
            f"Your Score: {self.__pong.ball.hit_count}", True, constants.WHITE
        )
        press_space_text = self.__font.render(
            "Press Space to play again", True, constants.WHITE
        )
        self.__window.fill(constants.BLACK)
        self.__window.blit(
            gameover_text,
            (
                (constants.WINDOW_WIDTH - gameover_text.get_width()) // 2,
                constants.WINDOW_HEIGHT // 2 - gameover_text.get_height() - 10,
            ),
        )
        self.__window.blit(
            score_text,
            (
                (constants.WINDOW_WIDTH - score_text.get_width()) // 2,
                constants.WINDOW_HEIGHT // 2 ,
            ),
        )
        self.__window.blit(
            press_space_text,
            (
                (constants.WINDOW_WIDTH - press_space_text.get_width()) // 2,
                constants.WINDOW_HEIGHT // 2 + press_space_text.get_height() + 10,
            ),
        )

    def cleanup(self):
        """Quit the game."""
        pygame.quit()
