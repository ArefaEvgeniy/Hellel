def my_decorator(a_func):
    def the_wrapper():
        print("Before")
        a_func()
        print("After")

    return the_wrapper


def my_decorator_2(a_func):
    def the_wrapper():
        print("Before 2")
        a_func()
        print("After 2")

    return the_wrapper


@my_decorator
@my_decorator_2
def alone_func():
    print("I am alone function")


# alone_func()
#
# print("-" * 50)
#
# alone_func = my_decorator(alone_func)

alone_func()
