def func(a, b, *args, x):
    print('args:', args)
    # for item in args:
    #     print(item)
    print('a:', a)
    print('b:', b)
    print('x:', x)
    # print('c:', c)
    # print('d:', d)
    # print('e:', e)
    # return str(a) + str(e)


a = 66
z = func(1, 5, 'RRR', 777, x=None)
print('-' * 50)
print('a:', a)
print('z:', z)