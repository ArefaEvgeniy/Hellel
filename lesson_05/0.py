a = 5

if a < 2:
    print('True')
    a += 1
    print('New a:', a)
    if a > -100:
        print('YES')
        a = -30
elif a > 10:
    print('a > 10')
    if a < 100:
        print('NO')
elif a == 5:
    print('a == 5')
elif a is 6:
    print('a is 6')
elif a in [3, 4, 5]:
    print('a in [3, 4, 5]')
else:
    print('a in {2-10}')

print('Finish')

res = 'Yes' if a == 5 else 'No'

if a == 5:
    res = 'Yes'
else:
    res = 'No'

print(res)

is_nice = True
state = 'nice' if is_nice else 'not nice'

nice = True
personality = ("вредная", "добрая")[nice]
print("Кошка", personality)
