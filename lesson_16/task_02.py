# Создать объект-итератор, который при инициализации получает 2 значения:
# минимальное и максимальное. При каждом обращении он должен возвращать
# значения по порядку от минимального до максимального.


class Counter:
    def __init__(self, low, high):
        self.current = low - 1
        self.high = high

    def __next__(self):
        if self.current < self.high:
            self.current += 1
            return self.current
        raise StopIteration


a = Counter(2, 7)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
