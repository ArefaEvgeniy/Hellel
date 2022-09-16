def simple_generator(valuem):
    while valuem > 0:
        valuem -= 1
        yield valuem ** 3


gen_iter = simple_generator(5)
# print(gen_iter)
# print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))

for item in simple_generator(5):
    print(item)

