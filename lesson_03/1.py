# Создать два списка произвольного содержания.
# Добавить к каждому списку по одному элементу в конец и в начало.
# Расширить первый список вторым.
# Все изменения выводить на экран.


a = list((1, 2, 3, 4, 's'))
b = ['a', 'b', 'c']

print('list a:', a, type(a))
print('list b:', b, type(b))

a.insert(0, 0)
a.append(9)
b.insert(0, 'x')
b.append('z')

print('list a:', a, type(a))
print('list b:', b, type(b))

a.extend(b)
print('list a:', a, type(a))
