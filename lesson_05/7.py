# Ввести два целых числа A и B.
# Вывести в порядке возрастания все целые числа,
# расположенные между A и B (включая сами числа A и B ),
# а также количество N этих чисел.

value_1 = input('Input first number: ')
value_2 = input('Input second number: ')

num_1 = int(value_1) if value_1.isdigit() else 0
num_2 = int(value_2) if value_2.isdigit() else 0

if num_1 > num_2:
    num_1, num_2 = num_2, num_1

N = 0
for item in range(num_1, num_2 + 1):
    print(item, end=' ')
    N += 1

print()
print('N =', N)
print('FINISH')

