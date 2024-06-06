class Ball:
    def __init__(self, x, y, radius, color):
        self.center = (x, y)
        self.radius = radius
        self.color = color

    def __repr__(self):
        return f"{self.color} ball with center at {self.center} and radius of {self.radius}"
