import pygame

## Paddle class for the Pong game
#
class Paddle:
    def __init__(self, pos_x: int, pos_y: int, width: int, height: int, speed: int):
        self.__posx = pos_x
        self.__posy = pos_y
        self.__width = width
        self.__height = height
        self.__speed = speed

    def move_left(self):
        self.__posx -= self.__speed

    def move_right(self):
        self.__posx += self.__speed

    def get_posx(self):
        return self.__posx

    def get_posy(self):
        return self.__posy

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height
    
    def display(self, window):
        pygame.draw.rect(window, (255, 255, 255), (self.__posx, self.__posy, self.__width, self.__height))

    
