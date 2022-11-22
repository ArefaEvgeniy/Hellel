try:
    res_1 = a / b
    res_2 = f / g
    res_3 = b / k
except ZeroDivisionError:
    print('Division on 0')
except TypeError:
    print('TypeError')
except (EOFError, TypeError):
    print('FFF')
else:
    print('ELSE')
finally:
    print('finally')

print(res_1)
print(res_2)
print(res_3)
