a_1 = [1, 2, 3, 4]
a_2 = list((1, 2, 3, 4))
a_3 = []
a_4 = list()

print(a_1)
print(type(a_1))
print(a_2)
print(type(a_2))
print(a_3)
print(type(a_3))
print(a_4)
print(type(a_4))

b_1 = [1, 2, 3, 4]
b_2 = [1, 2, 3, 4]
print('b_1:', b_1)
print('id of b_1:', id(b_1))
print('b_2:', b_2)
print('id of b_2:', id(b_2))

b_1.append('rr')
print('b_1:', b_1)
print('id of b_1:', id(b_1))

print(b_1[-1])

b_1.append(1)
print('b_1:', b_1)

z = b_1.remove(1)
print('b_1:', b_1)

del b_1[-2]
print('b_1:', b_1)

b_1[-1] = (1, 2, '44', None)
print('b_1:', b_1)

a = [1, 2, 3]
b = [4, 5, 6]

a.extend(b)
# a = a + b
print('a:', a)

a.insert(2, 'aa')
print('a:', a)

c = a.pop()
print('a:', a)
print('c:', c)
print('z:', z)

x = (1, 2, 3)
