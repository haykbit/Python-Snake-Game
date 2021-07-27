import pygame
from pygame.locals import *
import time
import random

SIZE = 30


class Apple:
    def __init__(self, surface):
        self.parent_screen = surface
        self.image = pygame.image.load("resources/apple-block.jpg").convert()
        self.x = SIZE*3
        self.y = SIZE*3

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(0, 28)*SIZE
        self.y = random.randint(0, 20)*SIZE


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


class Game:
    def __init__(self):
        pygame.init()
        # Create display 500px x 500px
        self.surface = pygame.display.set_mode((900, 700))
        # Background Color
        self.surface.fill((31, 31, 31))

        # Draw Snake
        self.snake = Snake(self.surface, 6)
        self.snake.draw()

        # Draw Apple
        self.apple = Apple(self.surface)
        self.apple.draw()

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.apple.move()

        for i in range(1, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "Game Over"

    def display_score(self):
        font = pygame.font.SysFont('Montserrat', 30)
        score = font.render(
            f"Score: {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(score, (700, 10))
        pygame.display.flip()

    def show_game_over(self):
        self.surface.fill((31, 31, 31))
        font = pygame.font.SysFont('Montserrat', 30)
        line1 = font.render(
            f"Game is over! Your score is: {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (300, 300))
        line2 = font.render(
            f"To play again press Enter", True, (255, 255, 255))
        self.surface.blit(line2, (300, 350))
        pygame.display.flip()

    def reset(self):
        self.snake = Snake(self.surface, 1)
        self.apple = Apple(self.surface)

    def run(self):
        # Screen live controller
        running = True
        pause = False
        while running:
            # event method
            for event in pygame.event.get():
                # This are methods from pygame.locals
                if event.type == KEYDOWN:

                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pause = False

                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()

                elif event.type == QUIT:
                    running = False
                    pause = True
            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(.3)


if __name__ == "__main__":
    game = Game()
    game.run()
