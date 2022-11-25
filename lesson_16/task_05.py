import pdb


def some_function(a, b, c):
    some_list = list()
    for i in range(a):
        pdb.set_trace()
        some_list.append(i * b / c)
        c = b * i
        b = c * i
    return some_list


print(some_function(5, 2, 3))
