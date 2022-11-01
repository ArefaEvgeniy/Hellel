f = open('example.txt', 'w')
f.write('Hello, world')
f.close()

f = open('example.txt', 'r')
try:
    print(f.read())
finally:
    f.close()

with open('example.txt', 'a') as f:
    f.write('\nПривет, world')

with open('example.txt', 'r') as f:
    print(f.read(17))
