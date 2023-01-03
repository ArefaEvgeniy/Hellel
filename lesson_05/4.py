# Метод str.find() возвращает индекс заданной подстроки в строке str,
# в случае неудачи он возвращает значение -1. Для списков не существует эквивалентного метода,
# но при желании мы могли бы создать такой функционал, использующую цикл while:

lst = ['a', 'f', 'r', 'sdfewf', 67, 8, 'hh', 0]

target = 'f'

index = 0
while index < len(lst):
    if lst[index] == target:
        break
    index += 1
else:
    index = -1

print('Index 1:', index)


for index, item in enumerate(lst):
    if item == target:
        break
else:
    index = -1

print('Index 2:', index)
