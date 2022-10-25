def my_decorator2(a_function):
    def wraper():
        print("<<<<<<")
        a_function()
        print(">>>>>>")

    return wraper


def my_decorator(a_function):
    def wraper():
        print("Before func")
        a_function()
        print("After func")

    return wraper


@my_decorator
@my_decorator2
def alone_func():
    print('I am alone function')


@my_decorator
def other_func():
    print('Hello, world!')


# other_func = my_decorator(other_func)

alone_func()
print('-' * 30)
other_func()
