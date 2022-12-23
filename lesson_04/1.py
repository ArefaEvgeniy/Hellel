import copy

first_list = [1, 'a', None, [1, 2, 3], 'tt']

first_copy = copy.deepcopy(first_list)
second_copy = copy.deepcopy(first_list)
# first_copy = first_list[:]
# second_copy = first_list[:]

print()

print('first_copy:', first_copy, 'id:', id(first_copy))
print('second_copy:', first_copy, 'id:', id(second_copy))

first_copy.append('new')
first_copy[3].append(4)

print('first_copy:', first_copy, 'id:', id(first_copy))
print('second_copy:', second_copy, 'id:', id(second_copy))
print('first_list:', first_list, 'id:', id(first_list))
