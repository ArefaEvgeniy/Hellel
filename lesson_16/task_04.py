import pdb


def some_function(v_1, v_2, v_3):
    some_list = list()
    for item in range(v_1):
        pdb.set_trace()
        some_list.append(item * v_2 / v_3)
        v_2 = v_3 * item
        v_3 = v_2 * item
    return some_list


print(some_function(5, 2, 3))
