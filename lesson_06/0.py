a = []

for i in range(1, 15):
    a.append(i)

print(a)

b = [i for i in range(1, 15)]

print(b)

x = [1, 2, -2, 4, -6, 6, 0]

y = [i**2 for i in x if i > 1]

print(y)

x_1 = {1: 10, 2: 20, 3: 30}


print('-' * 30)
y_1 = [i*x_1[i] for i in x_1]
y_2 = [[i, x_1[i]] for i in x_1]
y_3 = [j for i in y_2 for j in i]

print(y_1)
print(y_2)
print(y_3)
print('-' * 30)

z = 'fUKdhj345ioERdgvnfdl65eASDwi89854tlkdglbQEk45uitrylkmgf2u8t45'

z_int = [int(i) for i in z if i.isdigit()]
z_int_2 = [int(i) for i in z if '0'<=i<='9']
z_int_3 = [i for i in z if 'A'<=i<='Z']

print(z_int)
print(z_int_2)
print(z_int_3)
