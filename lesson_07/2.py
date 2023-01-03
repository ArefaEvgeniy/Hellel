def func(a, b, c=0, d='ddd', e='wefjywgf'):
    print('a:', a)
    print('b:', b)
    print('c:', c)
    print('d:', d)
    print('e:', e)
    return str(a) + str(e)


a = 66
z = func(1, a, 6, e=10)
print('-' * 50)
print('a:', a)
print('z:', z)
