import copy

a = [1, 3, 5, ['a', 'f', 'c'], 6]
b = copy.deepcopy(a)

print(a)
print(id(a))
print(b)
print(id(b))

print('-' * 50)
print(id(a[3]))
print(id(b[3]))
print('-' * 50)

a.append(7)
b.insert(0, 0)
a[3].append('d')

print(a)
print(b)
