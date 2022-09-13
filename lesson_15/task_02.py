def summa(x, y):
    result = None
    try:
        result = int(x) + int(y)
    except ValueError:
        result = x + y
    except Exception as err:
        print(err)
    else:
        print('else')
    finally:
        print('finally')

    return result


a = input("Введите первое значение: ")
b = input("Введите второе значение: ")

print(summa(a, b))

try:
    pass
finally:
    pass
