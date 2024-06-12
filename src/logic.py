import random
from objects import ball


class Game_Master:
    def __init__(self, screen, seed=None):
        self.screen = screen
        self.balls = []
        random.seed(seed)

    def initialize_balls(self, number, radius, velocity):
        while len(self.balls) != number:
            random_x = random.randint(
                radius, self.screen.get_width() - (radius))
            random_y = random.randint(
                radius, self.screen.get_height() - (radius))
            center = (random_x, random_y)
            v = (random.choice([-1, 1]) * velocity,
                 random.choice([-1, 1]) * velocity)
            color = random.choice(["red", "white", "blue"])
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

    def ball_collisions(self):
        for current_ball in self.balls:
            for target_ball in self.balls:
                if current_ball.collision_check(target_ball):
                    self.collision_outcome(current_ball, target_ball)
                    break

    def collision_outcome(self, ball_1, ball_2):
        if (
            (ball_1.color == "red" and ball_2.color == "white")
            or (ball_1.color == "white" and ball_2.color == "blue")
                or (ball_1.color == "blue" and ball_2.color == "red")):
            self.balls.remove(ball_2)
        """
        if ball_1.color == ball_2.color:
            ball_1.counter += 1
        if ball_1.counter == 700:
            ball_1.counter = 0
            random_x = random.randint(
                ball_1.radius, self.screen.get_width() - (ball_1.radius))
            random_y = random.randint(
                ball_2.radius, self.screen.get_height() - (ball_2.radius))
            center = (random_x, random_y)
            v = (random.choice([-1, 1]) * ball_1.velocity[0],
                 random.choice([-1, 1]) * ball_2.velocity[1])
            self.balls.append(ball(center, v, ball_1.radius,
                              ball_2.color, self.screen))
        """
