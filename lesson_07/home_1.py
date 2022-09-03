# Дан список чисел.
# Посчитать сколько раз встречается каждое число. Использовать для подсчёта функцию.
# Подсказка: для хранения данных использовать словарь (ключ - само число,
# а значение - сколько раз оно встречается). Для проверки нахождения элемента
# в словаре использовать метод get(), либо оператор in.


from random import randint


# Генерация случайного списка
numbers = []
for _ in range(50):
    numbers.append(randint(1, 10))
print("Первоначальный список: ", numbers)


def entries_count(sequence: list) -> dict:
    """Функция подсчета кол-ва чисел в списке"""
    result = {}
    for item in sequence:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


result = entries_count(numbers)
for item in result:
    print(f"Число {item} встречается в первоначальном списке "
          f"{result[item]} раз")
