# Сделать программу в виде функций в которой нужно будет угадывать число.


from random import randint

num_rand = randint(1, 10)
for i in range(1, 4):
    num_input = input('Введите число от 1 до 10: ')

    if num_input.isdigit():
        num_input = int(num_input)
    else:
        print("Введено не число, зря потратили попытку")
        continue

    if num_input < num_rand:
        print("Введённое число меньше загаданного")
    elif num_input > num_rand:
        print("Введённое число больше загаданного")
    else:
        print("Поздравляю! Вы угадали!!!")
        break

else:
    print(f"Вы исчерпали все попытки, загаданное число: {num_rand}")
