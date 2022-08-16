a = [1, 2, 3, 4]


def example(b=None):
    if b is None:
        b = [1, 2]
    print('b before:', b)
    sum = 0
    for item in b:
        sum += item
    b.append(sum)
    print('b after:', b)
    return sum


print(example())
print('-' * 50)
print(example(a))
print('-' * 50)
print(example())
print('-' * 50)
print(example())
print('-' * 50)
print(example(a))
