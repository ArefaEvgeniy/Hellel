# Метод str.find() возвращает индекс заданной подстроки в строке str,
# в случае неудачи он возвращает значение -1. Для списков не существует эквивалентного метода,
# но при желании мы могли бы создать такой функционал, использующую цикл while:

target = input()
lst = ['112', 45, 56, 'rrr', None]

# index = 0
# while index < len(lst):
#     if str(lst[index]) == target:
#         break
#     index += 1
# else:
#     index = -1
#
# print("Index:", index)


for index, x in enumerate(lst):
    print(index, x)
    if x == target:
        break
else:
    index = -1

print("Index:", index)
