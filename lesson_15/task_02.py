x = 10
d = [11, 23, 45]
try:
    x - d[5]
except IndexError:
    print('Invalid Key')
except LookupError:
    print('LookupError')
