# Создать собственную версию встроенной функции sum().
# Функция sum() возвращает сумму всех элементов итерируемого объекта,
# переданных ей.


from functools import reduce


def custom_sum(first, second):
    return first + second ** 2


result = reduce(custom_sum, {1, 2, 3, 4, 5, 6, 7})
print(result)

result_2 = reduce(custom_sum, (1, 2, 3, 4, 5, 6, 7))
print(result_2)
