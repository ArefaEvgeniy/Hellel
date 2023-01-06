def my_decorator(a_function):
    def wrapper():
        print('Я - код который выполняется до ф-ции')
        a_function()
        print('Я - код который выполняется после ф-ции')

    return wrapper


@my_decorator
def alone_function():
    print('Я - одинокая ф-ция')


@my_decorator
def new_function():
    a = 2 + 4
    print('a =', a)


# alone_function()
# print("-" * 50)
# alone_function = my_decorator(alone_function)
alone_function()
print("-" * 50)
new_function()
