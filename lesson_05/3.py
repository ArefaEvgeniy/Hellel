# Вычислить факториал введённого числа


c = int(input("Введено число: "))

q = 0
result = 1
while c > q:
    q += 1
    result *= q
    print('q:', q)
    print('result:', result)
    print('-------')

print("Result is: ", result)

# result = 1
# for a in range(1, c+1):
#     result *= a
#
# print("Result is: ", result)

