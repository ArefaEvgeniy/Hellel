a = 1
b = 2.5
c = '2'
a1 = str(a)

print(a + b)
print(type(a))
print(type(b))
print(type(a + b))

print(str(a) + c)
print(type(str(a) + c))

print(a + int(c))
print(type(a + int(c)))

print(round(int(a1 + c) + b + 0.009, 2))

e = 13.6223456878994

print(round(e, 5))
