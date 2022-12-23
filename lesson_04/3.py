a = 'Evgeniy'

b = 'Hello, %s' % a

print(b)

a = 6
b = 'bananas'
c = 10
d = 'lemons'

print('%d %s, %d-%s' % (a, b, c, d))

template = 'Меня зовут %(a)s. Мне %(b)d года. %(a)s - красивое имя.'
name = 'Evgeniy'
age = 42

print(template % {'a': name, 'b': age})

print('-' * 50)

template_2 = 'Меня зовут {a}. Мне {b} года. {a} - красивое имя.'
print(template_2.format(a=name, b=age))

cord = (3, 5)
print('X:{0[0]}; Y:{0[1]}, name - {1}'.format(cord, name))

print('{:<30} New text'.format(name))
print('{:>30} New text'.format(name))
print('{:^30} New text'.format(name))
print('{:*^30} New text'.format(name))


points = 19.5
total = 22

print('Percents: {:.2%}'.format(points/total))

print('-' * 50)

print(f'Меня зовут {name}. Мне {age} года. {name} - красивое имя.')

print(f'Percents: {points/total:.2%}')
print(f'{name:*^30} New text')

