class DimaException(BaseException): pass


a = 10
b = 3
c = a / b

if a % b != 0:
    raise DimaException('TEST')

print('Result:', c)
