name = "Tom"
print("Id name:", id(name))


def say_hi():
    def say_ops():
        print("Ops", name)

    name = "Bob"
    print("Id name:", id(name))
    print("Hello", name)
    say_ops()


def say_bye():
    global name
    name = 'Jack'
    print("Id name:", id(name))
    print("Good bye", name)


def say_good_morning():
    print("Id name:", id(name))
    print("Good morning", name)


say_hi()
say_bye()
say_good_morning()
