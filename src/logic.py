import random
from objects import ball


class Game_Master:
    def __init__(self, screen):
        self.screen = screen
        self.balls = []

    def generate_balls(self, number, radius, color):
        for i in range(number):
            random_x = random.randint(0, self.screen.get_width())
            random_y = random.randint(0, self.screen.get_height())
            center = (random_x, random_y)
            self.balls.append(ball(center, radius, color))
        return self.balls
