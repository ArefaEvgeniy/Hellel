def func(a, b, *args, e, **kwargs):
    print('args:', args)
    print('kwargs:', kwargs)
    for key in kwargs:
        print(f'{key}: {kwargs[key]}')
    print('a:', a)
    print('b:', b)
    # print('c:', c)
    # print('d:', d)
    print('e:', e)
    # return str(a) + str(e)


a = 66
z = func(555, 777, e=10, c=a, d=0)
print('-' * 50)
print('a:', a)
print('z:', z)
