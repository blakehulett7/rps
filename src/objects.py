class ball:
    def __init__(self, center, radius, color):
        self.center = center
        self.radius = radius
        self.color = color

    def __repr__(self):
        return f"{self.color} ball at {self.center} with radius {self.radius}"
