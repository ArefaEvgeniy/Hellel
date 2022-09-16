def simple_generator(valuem):
    while True:
        valuem += 1
        yield valuem ** 3


for item in simple_generator(0):
    if item > 1000:
        break
    print(item)
