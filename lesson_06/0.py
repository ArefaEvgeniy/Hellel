def summa(a, b):
    print('a: ', a)
    print('b: ', b)
    return a + b


def summa_2(a, b=1):
    return a + b, a**2, b - 1


def print_name(name):
    def upper_name(name):
        new_name = name.upper()
        return new_name

    print(f'Wellcome, {upper_name(name)}')


x = 4
y = 3
z = summa(x, y)
print(f'summa: {z}')

print(f'summa: {summa("ad", "bc")}')

print_name('Bob')

n = summa(x, y)

print('-' * 50)

a1, *a2 = summa_2(4)
print(a1)
print(a2)

b1 = list(summa_2(4))
print(b1)


def rrr(*args):
    print(args)
    for item in args:
        print(item)


rrr(1, 2, 3, 4, 5)
print('-' * 50)
rrr()
print('-' * 50)


def sss(**kwargs):
    print(kwargs)
    for item in kwargs:
        print(item)
        print(kwargs[item])


sss(a=2, b=7, t=3)
print('-' * 50)
sss()
print('-' * 50)


def ddd(*args, **kwargs):
    print(args)
    print(kwargs)


print('-' * 50)

ddd(2, 'dd', 'ty', None, True, w=112, g4='ty')
print('-' * 50)
ddd()
