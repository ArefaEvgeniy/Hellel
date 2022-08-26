f = open('test.txt')
a = f.read()
f.close()
print(a)
print(type(a))

print('-' * 50)

with open('test.txt') as f:
    b = f.readlines()
print(b)
print(type(b))

print('-' * 50)

f = open('test.txt')
try:
    c1 = f.readline()
    print(c1)
    print(type(c1))
    c2 = f.readline()
    print(c2)
    print(type(c2))
finally:
    f.close()