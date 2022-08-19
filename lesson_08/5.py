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
        print("#помидоры#")
        func()
        print("~салат~")
    return wrapper


def sandwich(food="--ветчина--"):
    print(food)


print("call 1:")
sandwich()
print(end='\n\n')


@bread
@ingredients
def sandwich(food="--ветчина--"):
    print(food)


print("call 2:")
sandwich()
