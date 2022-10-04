# Создать два списка произвольного содержания.
# Добавить к каждому списку по одному элементу в конец и в начало.
# Расширить первый список вторым.
# Все изменения выводить на экран.

a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c']

a.insert(0, 0)
print(a)
a.append(6)
print(a)
a.insert(len(a), 7)
print(a)

b.insert(0, 'z')
print(b)
b.append('d')
print(b)

a.extend(b)
print(a)

a = {1, 3, 'red'}
a.add(5)
print(a)

