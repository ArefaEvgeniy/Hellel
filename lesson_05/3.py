# Вычислить факториал введённого числа

c = int(input())

q = 1
result = 1
while c > q:
    q += 1
    result *= q
    print('q:', q)
    print('result:', result)

print('-' * 50)
print('general result:', result)
