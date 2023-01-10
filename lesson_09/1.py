from datetime import datetime


def factirial_1(n):
    q = 0
    result = 1
    while n > q:
        q += 1
        result *= q
    return result


def factirial_2(n):
    if n == 0:
        return 1
    else:
        return n * factirial_2(n - 1)


aa = int(input())
time = datetime.now()
print(factirial_1(aa))
print('factirial_1: ', datetime.now() - time)

time = datetime.now()
print(factirial_2(aa))
print('factirial_2: ', datetime.now() - time)