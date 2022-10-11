# Ввести два целых числа A и B.
# Вывести в порядке возрастания все целые числа,
# расположенные между A и B (включая сами числа A и B ),
# а также количество N этих чисел.


value_1 = int(input('Введите первое число: '))
value_2 = int(input('Введите второе число: '))

if value_1 > value_2:
    value_1, value_2 = value_2, value_1

# N = 0
for index, item in enumerate(range(value_1, value_2+1)):
    print(item, end=' ')
    # N += 1

print()
print('index:', index+1)

# range(10)  ->  (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
