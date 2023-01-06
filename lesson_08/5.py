# Написать декоратор, который выдаст:
# </----------\>
# помидоры
# --ветчина--
# ~салат~
# <\______/>


def bread(func):
    def wrapper():
        print("</----------\>")
        func()
        print("<\______/>")
    return wrapper


def ingredients(func):
    def wrapper():
        print("помидоры")
        func()
        print("~салат~")
    return wrapper


@bread
@ingredients
def my_func(food="--ветчина--"):
    print(food)


my_func()
