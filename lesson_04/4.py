# Запросить у пользователя два целых числа.
# Вывести строку вида "2 плюс 3 равно 5"

import datetime

num_1 = int(input('Enter first number: '))
num_2 = int(input('Enter second number: '))

NOW = datetime.datetime.now()
print('%d плюс %d равно %d' % (num_1, num_2, num_1 + num_2))
print('Time spend for %: ', datetime.datetime.now() - NOW)
NOW = datetime.datetime.now()
print('{} плюс {} равно {}'.format(num_1, num_2, num_1 + num_2))
print('Time spend for format: ', datetime.datetime.now() - NOW)
NOW = datetime.datetime.now()
print(f'{num_1} плюс {num_2} равно {num_1 + num_2}')
print('Time spend for f-string: ', datetime.datetime.now() - NOW)


b = 56
sales_tax_10 = 1.10
