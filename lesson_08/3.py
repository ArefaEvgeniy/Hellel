# Создать собственную версию встроенной функции sum().
# Функция sum() возвращает сумму всех элементов итерируемого объекта,
# переданных ей.


from functools import reduce


numbers = {1: 'r', 3: 'ttrt', 56: 'sd', 34: 'dfgds'}


result = reduce(lambda a, x: a + x, numbers)
print(result)
