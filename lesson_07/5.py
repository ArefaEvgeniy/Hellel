name = 'Tom'


print('Global name:', name)

def say_hi():
    name = 'Jack'
    def say():
        global name
        name = 'Bob'
        print('!!!,', name)
    say()
    print('Hello,', name)


def say_bye():
    print('Good bye,', name)


say_hi()
say_bye()
