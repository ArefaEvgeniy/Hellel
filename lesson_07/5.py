def area1(b, h):
    return 0.5 * b * h


area2 = lambda b, h:  0.5 * b * h

print(area1(3, 6))
print(area2(3, 6))


def test1(number):
    return str(number) if number == 1 else str(number) + 's'


test2 = lambda number: str(number) if number == 1 else str(number) + 's'

print(test1(1))
print(test2(1))
print(test1(10))
print(test2(10))
