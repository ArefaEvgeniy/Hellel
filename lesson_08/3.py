# Создать собственную версию встроенной функции sum().
# Функция sum() возвращает сумму всех элементов итерируемого объекта,
# переданных ей.

from functools import reduce


list_in = [1, 0, 56, 34, -6, 34, -103, 67]


def custom_sum(x, y):
    return x + y


result = reduce(custom_sum, list_in)
print(result)

result_2 = reduce(lambda x, y: x + y, list_in)
print(result_2)
