import copy


input_list = [1, 'a', 3, ['a', 'b'], '4']

first = copy.deepcopy(input_list)
second = copy.deepcopy(input_list)

print('first:', first)
print('second:', second)

first[3].append('new')

print('*' * 50)
print('first:', first)
print('second:', second)
