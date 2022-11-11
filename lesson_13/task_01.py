# Создать класс Point, который хранит координаты х и у,
# умеет вычислять расстояние от начала координат,
# может сравнивать координаты двух точек
# и при вызове через функцию принт возвращает свои координаты


import math


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __str__(self):
        return (f"Point({self.x}, {self.y})")

    def distance_from_origin(self):
        return math.hypot(self.x, self.y)


if __name__ == '__main__':
    a = Point(5, 4)
    b = Point(0, 5)

    print(a == b)

    b.y = 4

    print(a == b)

    c = a + b

    print('distance c:', c.distance_from_origin())

    print(a)
    print(b)
    print(c)
