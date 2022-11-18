class Car:
    last_model = None

    def __init__(self, model):
        self.model = model
        Car.last_model = model


# print('Car.last_model:', Car.last_model)
car_1 = Car('BMW')
# print('Car.last_model:', Car.last_model)
car_2 = Car('Mersedes')
# print('Car.last_model:', Car.last_model)
car_3 = Car('FIAT')
print('Car.last_model:', Car.last_model)
