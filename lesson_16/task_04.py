def simple_generator(value):
    while value > 0:
        value -= 1
        yield "GO"


a = simple_generator(5)
for item in a:
    print(item)
