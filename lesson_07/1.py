def test(x, y, z=5):
    print('x:', x)
    print('y:', y)
    print('z:', z)
    return str(x) + str(y) + str(z)


a = test(1, z=9, y='dd')
print(a)


def test_2(*args):
    result = ''
    print('args:', args)
    for item in args:
        result += ' ' + str(item)
    return result


res = test_2(1, 4, 'r', '!')
print('res:', res)
print('type:', str(type(res)))


def test_3(**kwargs):
    result = 0
    print('kwargs:', kwargs)
    for item in kwargs:
        result += kwargs[item]
    return result


res_2 = test_3(y=1, x=0, a=6, t=66)
print('res_2:', res_2)

print('-' * 50)


def test_4(*args, **kwargs):
    print('args:', args)
    print('kwargs:', kwargs)
    return 'f', 'h'


a = test_4(1, 3, 4, 6, t=6, w=33)
print('a:', a)

s = [1, 5, 7, 't', 'w' 'r']

print('s:', s)
print('len:', len(s))
