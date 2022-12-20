# !!! Это задание выполнять не надо!!!
# Это разбор предыдущего домашнего задания
# Ввести с клавиатуры целое число number.
# Получить сумму кубов всех целых чисел от 1 до number(включая number).
# Исключения составляют все числа кратные цифре 3.
# Реализовать в 2-х вариантах: используя цикл while и цикл for


while True:
    n = input('insert  value')
    if not n.isdigit() or n == 0:
        print('try one more time')
    else:
        n = int(n)

    # Операторы циклов While
    i = 1
    ksum = 0
    while i <= n:
        if i % 3 == 0:
            continue
        else:
            a = i ** 3
            ksum = a + ksum
            i += 1
    print(ksum)

    ksum = 0
    exception1 = 0
    for n in range(n):
        exception1 = n % 3
        if exception1 == 0:
            continue
        a = n ** 3
        ksum = a + ksum
    print(ksum)

    print('Желаете выйти? (Д/Y): ')
    print('Желаете продолжить нажмите Enter: ')
    a = input()
    if a == 'Y':
        break
    elif a == 'Д':
        break
    else:
        continue
