import pygame
import math


class ball:
    def __init__(self, center, velocity, radius, color, screen):
        self.center = center
        self.velocity = velocity
        self.radius = radius
        self.color = color
        self.screen = screen

    def __repr__(self):
        return f"{self.color} ball at {self.center} with radius {self.radius} and velocity {self.velocity}"

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.center, self.radius)

    def collision_check(self, target_ball):
        a_sq = (self.center[0] - target_ball.center[0]) ** 2
        b_sq = (self.center[1] - target_ball.center[1]) ** 2
        distance = math.sqrt(a_sq + b_sq)
        return distance < (self.radius + target_ball.radius)
