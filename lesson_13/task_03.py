class Animal:
    viviparous = True

    def __init__(self, name, number_of_foot=4, tail=True):
        self.name = name
        self.number_of_foot = number_of_foot
        self.tail = tail

    def go(self):
        for item in range(1, self.number_of_foot + 1):
            print(f'step {item}')


class Dog(Animal):
    def say(self):
        print('Woof, woof')


class Cat(Animal):
    def say(self):
        print('Miay!')


class Dolphin(Animal):
    def __init__(self, name, number_of_foot=0, tail=True, fin=True):
        super().__init__(name, number_of_foot, tail)
        self.fin = fin

    def say(self):
        print('ultrasound')

    def go(self):
        print('Swim')


class Monster(Dog, Dolphin):
    ...

