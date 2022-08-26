# Имеется текстовый файл. Напечатать:
# a) его первую строку;
# b) его пятую строку;
# c) его первые 5 строк;
# d) весь файл.


f = open('test.txt')

data_a = f.readline()
print(f'first line: {data_a}')
f.close()

f = open('test.txt')
for index, item in enumerate(f):
    if index == 4:
        print(f'fives line: {item}')
f.close()

f = open('test.txt')
for index, item in enumerate(f):
    if index <= 4:
        print('lines:', item, end='')
f.close()

print('-' * 50)

with open('test.txt') as f:
    a = f.readlines()
    for item in a:
        print(item, end='')
