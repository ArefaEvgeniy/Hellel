# Запросить у пользователя возраст.
# Если возраст меньше 0 или введено не число - вывести Wrong input
# Если возраст меньше или равен 12 - вывести Orange
# Если ввозраст больше 12 и меньше 18 - вывести CocaCola
# Иначе - вывести Beer


age = input("Введите ваш возраст: ")

if not age.isdigit() or int(age) <= 0:
    print('Wrong input')
elif int(age) <= 12:
    print('Orange')
elif int(age) < 18:
    print('CocaCola')
else:
    print('Beer')
