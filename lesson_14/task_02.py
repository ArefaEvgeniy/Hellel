class Car():
    number_of_models = 0

    def __init__(self, model):
        self.model = model
        Car.number_of_models += 1

    @classmethod
    def total_objects(cls):
        print("Total objects:", cls.number_of_models)


a = Car('blue')
b = Car('green')
c = Car('ZAZ')

a.total_objects()
Car.total_objects()
b.total_objects()
