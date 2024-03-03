import pygame
import random

# Import the Paddle class
import Paddle


## Ball class for the pong game
#
class Ball:
    def __init__(self, pos_x: int, pos_y: int, radius: int, speed_x: int, speed_y: int):
        self.__posx = pos_x
        self.__posy = pos_y
        self.__radius = radius
        self.__speedx = speed_x
        self.__speedy = speed_y
        self.__hit_count = 0

    def move(self):
        self.__posx += self.__speedx
        self.__posy += self.__speedy

    def get_posx(self):
        return self.__posx

    def get_posy(self):
        return self.__posy
    
    def get_hit_count(self):
        return self.__hit_count

    def display(self, window):
        pygame.draw.circle(
            window, (255, 255, 255), (self.__posx, self.__posy), self.__radius
        )

    def check_collision(self, paddle: Paddle, window: pygame.Surface):
        # check collision with the paddle
        if (
            self.__posy >= paddle.get_posy() - self.__radius
            and paddle.get_posx()
            <= self.__posx
            <= paddle.get_posx() + paddle.get_width()
        ):
            # track the number of hits
            self.__hit_count += 1
            # increase the speed of the ball after every 5 hits
            self.__speedx += self.__hit_count // 2
            self.__speedy += self.__hit_count // 2

            # change the direction of the ball
            self.__speedy = -abs(self.__speedy)

        # check collision with the side walls
        if self.__posx <= 0 or self.__posx >= window.get_width() - self.__radius:
            self.__speedx = -self.__speedx
        # check collision with the top wall
        if self.__posy <= 0:
            self.__speedy = -self.__speedy

        # check collision with the bottom wall
        if self.__posy >= window.get_height() - self.__radius:
            self.__speedy = -self.__speedy
            self.__hit_count = 0
            self.__speedx = random.choice([-3, 3])
            self.__speedy = 3
            self.__posx = window.get_width() // 2
            self.__posy = window.get_height() // 2
            print("Game Over")
            return False
        
        return True

