# Метод str.find() возвращает индекс заданной подстроки в строке str,
# в случае неудачи он возвращает значение -1. Для списков не существует эквивалентного метода,
# но при желании мы могли бы создать такой функционал, использующую цикл while:

lst = [1, 'aa', 4, 'fgt', 0]
target = 4

index = 0
while index < len(lst):
    if lst[index] == target:
        break
    index += 1
else:
    index = -1

print('index:', index)


for index, x in enumerate(lst):
    if x == target:
        break
else:
    index = -1

print('index 2:', index)
