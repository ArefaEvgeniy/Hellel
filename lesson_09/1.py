from datetime import datetime


def factorial_1(n):
    q = 0
    result = 1
    while n > q:
        q += 1
        result *= q
    return result


def factorial_2(n):
    if n == 0:
        return 1
    else:
        return n * factorial_2(n-1)


data = int(input('Input number: '))

time = datetime.now()
print(factorial_1(data))
print('time of factorial_1:', datetime.now() - time)
time = datetime.now()
print(factorial_2(data))
print('time of factorial_2:', datetime.now() - time)
