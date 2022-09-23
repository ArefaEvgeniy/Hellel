# Создать программу-калькулятор в виде класса и несколько методов,
# как минимум сложение, вычитание, деление, умножение, возведение в степень
# и извлечение квадратного корня.
# Обернуть каждый метод в блок try/except и сделать обработку нескольких
# исключений, как минимум деление на 0.
#
# Создать своё исключение, к примеру возведение в отрицательную степень.


class Negative_degree(Exception):
    def __init__(self, message='Возведение в отрицательную степень'):
        super().__init__(message)

class Calculator(int):

    def __init__(self, var):
        self.var = var

    def __add__(self, other):
        try:
            return Calculator(self.var + other)
        except TypeError:
            return 'Нельзя складывать цифры и буквы!'

    def __sub__(self, other):
        try:
            return Calculator(self.var - other)
        except TypeError:
            return 'Нельзя от цифры отнять буквы!'

    def __pow__(self, power, modulo=None):
        if power >= 0:
            return Calculator(self.var ** power)
        else:
            raise Negative_degree()

    def __truediv__(self, other):
        try:
            return Calculator(self.var / other)
        except ZeroDivisionError:
            return 'Нельзя делить на ноль!'
        except TypeError:
            return 'Нельзя нельзя делить на буквы!'
