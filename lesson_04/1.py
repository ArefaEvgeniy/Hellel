import datetime


name = 'Евгений'
age = 43
pi = 3.14159

s_file = open('test.txt', 'w')

print("Меня зовут %s, мне %d года" % (name, age))
print("Меня зовут %(dd)s, мне %(aa)d года. %(dd)s любит кашу." % {'dd': name, 'aa': age}, file=s_file, end='')
s_file.close()

print("Меня зовут {}, мне {} года".format(name, age))
print("Меня зовут {}, мне {} года. {} любит кашу.".format(name, age, name))

print("Меня зовут {0}, мне {1} года. {0} любит кашу.".format(name, age))
print("Меня зовут {name}, мне {age} года. {name} любит кашу.".format(name=name, age=age))

print(f"Меня зовут {name.upper()}, мне {age} года. {name.lower()} любит кашу.")
print(f'Число ПИ: {(pi * age):.3f}')


now = datetime.datetime.now()
print("Меня зовут %s, мне %d года" % (name, age))
print('Время выполнения: ', datetime.datetime.now() - now)

now = datetime.datetime.now()
print("Меня зовут {0}, мне {1} года".format(name, age))
print('Время выполнения: ', datetime.datetime.now() - now)

now = datetime.datetime.now()
print(f"Меня зовут {name}, мне {age} года")
print('Время выполнения: ', datetime.datetime.now() - now)
