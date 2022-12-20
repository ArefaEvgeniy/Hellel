a_1 = ()
a_2 = tuple()
a_3 = (1, 3, 'a', 3)
a_4 = tuple('rty')
a_5 = ('rty',)
b = 3
c = [1, 2, 3, 4]

print(a_1)
print(type(a_1))
print(a_2)
print(type(a_2))
print(a_3)
print(type(a_3))
print(a_4)
print(type(a_4))
print(a_5)
print(len(a_5))
print(type(a_5))

print(id(a_3))
print(id(a_3[0]))
print(id(a_3[1]))
print(id(a_3[2]))
print(id(a_3[3]))

print(id(b))
print(id(c[2]))

d = (1, 3, ('a', 'bb', ('cc',), None), True, (False, 4, 10))

print(d)
print(type(d))
print(len(d))

print(d[1])
print(d[2][0])

print(d[2][2][0][-1])
print(type(d[2][2][0][-1]))

print(d[0:3])
print(len(d[0:3]))

x_1 = 'text'
x_2 = 'text'

print(x_1)
print(id(x_1))

print(x_2)
print(id(x_2))
