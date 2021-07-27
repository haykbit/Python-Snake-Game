import pygame
from pygame.locals import *
import time
import random

SIZE = 30
SIZE_IMAGE = 10


class Apple:
    def __init__(self, surface):
        self.parent_screen = surface
        self.image = pygame.image.load("resources/apple-block.jpg").convert()
        self.x = SIZE_IMAGE*3
        self.y = SIZE_IMAGE*3

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(0, 30)*SIZE
        self.y = random.randint(0, 23)*SIZE


class Snake:
    def __init__(self, surface, length):
        # block length
        self.length = length
        # Parent screen for acces surface
        self.parent_screen = surface
        # Load image
        self.block = pygame.image.load("resources/snake-block.jpg").convert()
        # set multiple x and y cordinate
        self.x = [SIZE]*length
        self.y = [SIZE]*length
        # Set first direction
        self.direction = 'down'

    # method draw snake block
    def draw(self):
        self.parent_screen.fill((31, 31, 31))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):

        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE

        self.draw()
