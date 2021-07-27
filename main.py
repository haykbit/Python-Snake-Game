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
