from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, number_of_foot=4, tail=True):
        self.name = name
        self.number_of_foot = number_of_foot
        self.tail = tail

    @abstractmethod
    def say(self):
        ...

    def go(self):
        for item in range(1, self.number_of_foot + 1):
            print(f'step {item}')


class Dog(Animal):
    def say(self):
        print('Woof, woof')


dog_1 = Dog('Bob')
dog_1.go()
dog_1.say()
