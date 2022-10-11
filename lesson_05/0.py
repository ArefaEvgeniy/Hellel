a = 8

if a < 5:
    print('111')
elif a < 10:
    print('222')
    if a > 9:
        print('444')
    else:
        print('666')
elif a < 20:
    print('333')
else:
    print('000')

print('srer')


if a > 10:
    c = 'Yes'
else:
    c = 'No'

c = 'Yes' if a > 10 else 'No'


nice = True
pers = ('вредная', 'добрая')[nice]
print('Кошка', pers)
