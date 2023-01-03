def func_1():
    print('RUN FUNCTION')
    return 55


func_0 = 2222
print(id(func_0))
print(id(func_1))

print(func_0)
a = func_1()
print(a)
