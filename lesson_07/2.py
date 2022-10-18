a = 7


def test(x):
    print('x_1:', x)
    x = 66
    print('x_2:', x)


test(a)
print('a:', a)


b = [7, 2]
# print('b_1:', b)


def test(x=None):
    if x is None:
        x = list(range(1, 5))
    print('x_1:', x)
    x.append(77)
    print('x_2:', x)


test(b)
# print('b_2:', b)

test()
test()
test(b)
test()
test()
