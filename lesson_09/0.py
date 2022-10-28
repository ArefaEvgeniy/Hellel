import time
from datetime import datetime


def decorator_time(a_func):
    def wraper(*args, **kwargs):
        now = time.time()
        result = a_func(*args, **kwargs)
        all_time = round(time.time() - now, 5)
        print("Время выполнения функции: ",  all_time, "секунд")
        return result
    return wraper


@decorator_time
def sum_list():
    print('sum_list')
    return sum([number for number in range(10000)])


print(sum_list())


# @decorator_time
# def func(number):
#     print('func')
#     rez = 1
#     for num in range(1, number+1):
#         rez *= num
#     return rez
#
#
# print(func(1000))
