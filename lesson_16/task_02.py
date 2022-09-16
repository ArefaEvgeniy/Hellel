# Создать объект-итератор, который при инициализации получает 2 значения:
# минимальное и максимальное. При каждом обращении он должен возвращать
# значения по порядку от минимального до максимального.


class Counter(object):

    def __init__(self, low, high):
        self.current = low - 1
        self.high = high

    def __next__(self):
        self.current += 1
        if self.current <= self.high:
            return self.current
        raise StopIteration

    def __iter__(self):
        return self


a = Counter(2, 5)
# print('next:', next(a))
# print('next:', next(a))
# print('next:', next(a))
# print('next:', next(a))
# print('next:', next(a))

for item in a:
    print('for:', item)
