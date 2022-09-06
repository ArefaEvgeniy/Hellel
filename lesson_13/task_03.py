class Animal(object):
    viviparous = True
    number_of_foot = 4
    tail = True
    name = None

    def __init__(self, name, number_of_foot=4, tail=True):
        self.name = name
        self.number_of_foot = number_of_foot
        self.tail = tail

    def go(self):
        for item in range(1, self.number_of_foot+1):
            print(f'Step on {item} foot', end='-')
        print()


class Dog(Animal):
    _weight_1 = 10
    __weight_2 = 20

    def __str__(self):
        return f"Это класс собака, у него есть хвост и лапы"

    def say(self):
        print('Woof, woof')


class Cat(Animal):

    def say(self):
        print('Miay')


class Dolphin(Animal):
    fin = True
    number_of_foot = None

    def __init__(self, name='Noname', number_of_foot=3, tail=True, fin=True):
        super().__init__(name, number_of_foot, tail)
        self.fin = fin

    def say(self):
        print('Ultrasound')

    def go(self):
        print('Swim')
        super().go()
        print('Swim')

    def not_breath(self):
        print('No breath around 60 min')


class Monster(Dog, Dolphin):
    pass


monster_1 = Monster()
print(monster_1)
print(monster_1.name)
print(monster_1.say())
print(monster_1.go())
print(Monster.mro())
