x = 10
d = [1, 2, 3, 4]

try:
    a = x - d[5]
except IndexError as err:
    print('Индекс не существует', err)
except LookupError:
    print('Исключение LookupError')
except Exception as err:
    print(err)
