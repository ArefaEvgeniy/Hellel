# Имеется текстовый файл. Напечатать:
# a) его первую строку;
# b) его пятую строку;
# c) его первые 5 строк;
# d) весь файл.

with open('example.txt', 'r') as f:
    print(f.readline())

with open('example.txt', 'r') as f:
    for index, item in enumerate(f):
        if index == 4:
            print(item)

with open('example.txt', 'r') as f:
    for index, item in enumerate(f.readlines()):
        if index <= 4:
            print(item)

with open('example.txt', 'r') as f:
    print(f.read())
