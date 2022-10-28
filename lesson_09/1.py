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
        return n * factorial_2(n - 1)


now = datetime.now()
print(factorial_1(10000))
print(datetime.now() - now)

now = datetime.now()
print(factorial_2(990))
print(datetime.now() - now)
