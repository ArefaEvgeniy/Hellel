# Сделать программу в виде функций в которой нужно будет угадывать число.
# Программа с подвохом ;)


print("\nЯ загадал число от 1 до 10, отгадай его с трех попыток и получишь ПРИЗ")
while True:
    attempt = 1
    available_numbers = [x for x in range(1, 11)]
    while attempt <= 3:
        while True:
            choice = input(f"Попытка №{attempt}. Введи число от {min(available_numbers)}"
                           f" до {max(available_numbers)}: ")
            if choice.isdigit() and 1 <= int(choice) <= 10 \
                    and int(choice) in available_numbers:
                choice = int(choice)
                break
            else:
                print(f"Введи, пожалуйста, число от {min(available_numbers)} "
                      f"до {max(available_numbers)}\n")

        if available_numbers.index(choice) < int(len(available_numbers) / 2):
            print("Моё число больше твоего\n")
            available_numbers = available_numbers[available_numbers.index(choice) + 1:]
        else:
            print("Моё число меньше твоего\n")
            available_numbers = available_numbers[:available_numbers.index(choice)]
        attempt += 1
    print(f"Загаданное число было {available_numbers[0]}")
    if input("Увы, у тебя не получилось отгадать моё число. "
             "Хочешь попробовать ещё? (Y/N): ").capitalize() == "N":
        break
print("Повезёт в другой раз. До свидания =)")
