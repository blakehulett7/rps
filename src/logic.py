import random
from objects import Ball


class Game_Master:
    def __init__(self, screen_x, screen_y, canvas):
        self.balls = []
        self.screen_x = screen_x
        self.screen_y = screen_y
        self.canvas = canvas

    def generate_balls(self, number, color):
        for i in range(number):
            self.balls.append(Ball(random.randint(0, self.screen_x),
                                   random.randint(0, self.screen_y),
                                   50,
                                   "white"))

    def draw_balls(self):
        for ball in self.balls:
            ball.draw(self.canvas, ball.color)
