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

    def move(self):
        x = self.center[0]
        y = self.center[1]
        x += self.velocity[0]
        y += self.velocity[1]
        self.center = (x, y)

    def collision_check(self, target_ball):
        if self == target_ball:
            return False
        a_sq = (self.center[0] - target_ball.center[0]) ** 2
        b_sq = (self.center[1] - target_ball.center[1]) ** 2
        distance = math.sqrt(a_sq + b_sq)
        return distance < (self.radius + target_ball.radius)

    def wall_bounce(self):
        x = self.center[0]
        y = self.center[1]
        vel_x = self.velocity[0]
        vel_y = self.velocity[1]
        if x <= self.radius and vel_x < 0:
            vel_x *= -1
        if y <= self.radius and vel_y < 0:
            vel_y *= -1
        if x >= self.screen.get_width() - self.radius and vel_x > 0:
            vel_x *= -1
        if y >= self.screen.get_height() - self.radius and vel_y > 0:
            vel_y *= -1
        self.velocity = (vel_x, vel_y)
