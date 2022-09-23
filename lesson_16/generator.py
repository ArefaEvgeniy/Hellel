def my_func(value):
    print('my_func')
    result = value
    while True:
        result = result ** 2
        if result >= 15:
            result = int(result / 3)
        yield result


input_value = 2
for item in my_func(input_value):
    if item > 10000:
        break
    print(item)
