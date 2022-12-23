sourceFile = open('python.txt', 'w')

print('first', 'second', 3, sep='--', end='', file=sourceFile)
print('new value', 4)
print('55', 555)

a = input('Введите ваше имя: ')
print('Hello', a)
b = int(input('Введите ваш возраст: '))
print(type(b))
print('Вам через год будет', int(b) + 1, 'лет')
