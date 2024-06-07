import random
from objects import ball


class Game_Master:
    def __init__(self, screen, seed=None):
        self.screen = screen
        self.balls = []
        random.seed(seed)

    def initialize_balls(self, number, radius, color, velocity):
        while len(self.balls) != number:
            random_x = random.randint(
                radius, self.screen.get_width() - (radius))
            random_y = random.randint(
                radius, self.screen.get_height() - (radius))
            center = (random_x, random_y)
            v = (random.choice([-1, 1]) * velocity,
                 random.choice([-1, 1]) * velocity)
            current_ball = ball(center, v, radius, color, self.screen)
            if not self.collision_check(current_ball):
                self.balls.append(current_ball)

    def collision_check(self, ball_to_check):
        collisions = []
        for target_ball in self.balls:
            collisions.append(ball_to_check.collision_check(target_ball))
        return True in collisions

    def draw_balls(self):
        for current_ball in self.balls:
            current_ball.draw()

    def move_balls(self):
        for current_ball in self.balls:
            current_ball.move()

    def wall_collisions(self):
        for current_ball in self.balls:
            current_ball.wall_bounce()
