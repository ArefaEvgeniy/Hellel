# Создать 2 класса truck и car, которые являются наследниками класса auto.
# Класс truck имеет дополнительный обязательный атрибут max_load.
# Переопределённый метод move, перед появлением надписи «move» выводит
# надпись «attention», его реализацию сделать при помощи оператора super.
# А так же дополнительный метод load. При его вызове происходит пауза 1 сек.,
# затем выдаётся сообщение «load» и снова пауза 1 сек.
# Класс car имеет дополнительный обязательный атрибут max_speed и при вызове
# метода move, после появления надписи «move» должна появиться надпись
# «max speed is <max_speed>». Вместо <max_speed> должно выводится значение
# обязательного атрибута max_load.
# Создать по 2 объекта для каждого из классов truck и car,
# проверить все их методы и атрибуты.


import time
from home_1 import Auto

class Truck(Auto):
    def __init__(self, brand, age, mark, max_load, color=None, weight=None):
            super().__init__(brand, age, mark, color, weight)
            self.max_load = max_load

    def move(self):
            print("attention")
            super().move()

    def load(self):
            time.sleep(1)
            print("load")
            time.sleep(1)


class Car(Auto):
    def __init__(self, brand, age, mark, max_speed, color=None, weight=None):
            super().__init__(brand, age, mark, color, weight)
            self.max_speed = max_speed

    def move(self):
        super().move()
        print(f"max speed is {self.max_speed}")
