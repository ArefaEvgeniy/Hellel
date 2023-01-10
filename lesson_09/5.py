a = [8, 5, 4, 5]


def func(d):
    print("d before:", d)
    d.append(0)
    d.append(3)
    print("d after:", d)


print("a before:", a)
func(a)
print("a after:", a)

print('-' * 50)


def func_2(d=None):
    if d is None:
        d = [1, 2, 3]
    d.append(len(d))
    return d


print(func_2([9, 6, 5, 4]))
print(func_2())
print(func_2([]))
print(func_2())
print(func_2())
