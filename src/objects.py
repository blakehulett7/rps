import pygame


class ball:
    def __init__(self, center, radius, color, screen):
        self.center = center
        self.radius = radius
        self.color = color
        self.screen = screen

    def __repr__(self):
        return f"{self.color} ball at {self.center} with radius {self.radius}"

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.center, self.radius)
