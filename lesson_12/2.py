class Dog:
    def __init__(self, name, age, weight):
        self.__name = name
        self._age = age
        self.weight = weight


dog_1 = Dog('Bob', 4, 24)
print(dog_1.weight)
print(dog_1._age)
print(dog_1._Dog__name)
