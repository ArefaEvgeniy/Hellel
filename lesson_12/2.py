from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def say(self):
        pass

    def go(self):
        print('GO')


class Dog(Animal):
    number_of_foot = 4

    def say(self):
        print('Woof, woof')


dog_1 = Dog()
dog_1.go()
dog_1.say()
