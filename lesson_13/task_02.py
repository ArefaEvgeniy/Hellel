# Создать класс Circle на базе класса Point
# Класс должен поддерживать все методы родительского класса, а так же:
# минимальное расстояние от окружности до центра координат;
# площадь окружности и длину окружности.


import math
from task_01 import Point


class Circle(Point):
    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __add__(self, other):
        # center = super().__add__(other)
        x = self.x + other.x
        y = self.y + other.y
        radius = self.radius + other.radius
        return Circle(radius, x, y)

    def __str__(self):
        return 'Circle' + super().__str__()[5:] + f', radius={self.radius}'

    def area(self):
        return math.pi * (self.radius ** 2)

    def circle_weight(self):
        return 2 * math.pi * self.radius


m = Circle(6, 2, 3)
n = Circle(3)
l = Circle(6, 5, 7)

print(m == n)
print(m == l)

z = m + l   # Circle(12, 7 ,10)

print(m)
print(n)
print(l)
print(z)
