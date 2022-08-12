# !!! Это задание выполнять не надо!!!
# Это разбор предыдущего домашнего задания
# Ввести с клавиатуры целое число n.
# Получить сумму кубов всех целых чисел от 1 до n(включая n).
# Исключения составляют все числа кратные цифре 3.
# Реализовать в 2-х вариантах: используя цикл while и цикл for


while True:
    # Операторы циклов While
    digit1 = input('insert  value')
    if not digit1.isdigit() or digit1 == 0:
        print('try one more time')
    else:
        digit1 = int(digit1)

    counter = 0
    ksum = 0
    while True:
        if counter == digit1:
            break
        counter += 1
        if counter % 3 == 0:
            continue
        else:
            a = counter ** 3
            ksum = a + ksum
            print(ksum)

    # Оператор For
    digit1 = input('insert  value')
    if not digit1.isdigit() or digit1 == 0:
        print('try one more time')
    else:
        digit1 = int(digit1)

    ksum = 0
    exception1 = 0
    for digit1 in range(digit1):
        exception1 = digit1 % 3
        if exception1 == 0:
            continue
        a = digit1 ** 3
        ksum = a + ksum
    print(ksum)

    print('Желаете выйти? (Д/Y): ')
    print('Желаете продолжить нажмите Enter: ')
    answer = input()
    if answer in ('y', 'Y', 'д', 'Д'):
        break
    else:
        continue

names = 'Bob Jack'
list_of_names = names.split()

while True:
    # Операторы циклов While
    input_str = input('insert  value')
    if not input_str.isdigit() or int(input_str) == 0:
        print('try one more time')
        continue

    input_int = int(input_str)
    counter = 0
    kub_sum = 0
    while True:
        if counter == input_int:
            break
        counter += 1
        if counter % 3 == 0:
            continue
        kub_sum += counter ** 3

    print(kub_sum)

    # Оператор For
    ksum = 0
    for item in range(1, input_int+1):
        if item % 3 == 0:
            continue
        ksum += item ** 3
    print(ksum)

    answer = input('Желаете выйти? (Д/Y)\nЖелаете продолжить нажмите Enter: ')
    if answer.upper() in ('Y', 'Д'):
        break

