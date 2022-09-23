# Создать генератор геометрической прогрессии


def simple_generator(start, step):
    val = start
    yield val
    while True:
        val *= step
        yield val


for item in simple_generator(-2, -5):
    print(item)
    if -1000 <= item >= 1000:
        break
