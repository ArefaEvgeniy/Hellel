# Вычислить факториал введённого числа


number = int(input())
q = 0
result = 1
while number > q:
    q += 1
    result *= q

print('result:', result)
