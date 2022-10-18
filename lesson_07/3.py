name = 'Tom'


def say_hi():
    global name
    name = 'Jack'
    print('Hello,', name)


def say_bye():
    print('Good bye,', name)


say_hi()
say_bye()
