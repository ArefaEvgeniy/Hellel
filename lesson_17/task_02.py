import math


class Circle(object):

    def __init__(self, radius, x=0, y=0):
        self.x = x
        self.y = y
        self.radius = radius

    def distance_from_origin(self):
        return math.hypot(self.x, self.y)

    def edge_distance_from_origin(self):
        return abs(self.distance_from_origin() - self.radius)

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        radius = self.radius + other.radius
        return Circle(radius, x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        radius = abs(self.radius - other.radius)
        return Circle(radius, x, y)

    def __str__(self):
        return f'Circle({self.x}, {self.y}), radius={self.radius})'

