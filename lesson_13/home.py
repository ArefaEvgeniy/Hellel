# *Для рассмотренного на уроке класса Circle реализовать метод производящий
# вычитание двух окружностей, вычитание радиусов произвести по модулю.
# Если вычитаются две окружности с одинаковым значением радиуса,
# то результатом вычитания будет точка класса Point.


import math
from task_01 import Point

class Circle(Point):
    radius = 0
    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

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
        return Circle(radius, x, y) if radius else Point(x, y)

    def __str__(self):
        return super().__str__()[:-1] + f', radius={self.radius})'


circle_1 = Circle(6, 2, 4)
circle_2 = Circle(3)
print('circle_1: ', circle_1)
print('circle_2: ', circle_2)
circle_3 = circle_1 - circle_2
print('circle_3: ', circle_3)
print(str(type(circle_3)))
circle_4 = circle_3 - circle_2
print('circle_4: ', circle_4)
print(str(type(circle_4)))
