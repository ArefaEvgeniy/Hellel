# Ввести число, проверить на то, что было введено именно число.
# Возвести его в куб.
# Реализацию обернуть в вечный цикл с возможностью выйти из него по запросу.


while True:
    input_value = input("Введите число: ")
    if not input_value.isdigit():
        continue

    print("Куб числа: ", int(input_value)**3)

    answer = input("Хотите выйти? (Y/Д): ")
    if answer.upper() in ('Y', 'Д'):
        break
