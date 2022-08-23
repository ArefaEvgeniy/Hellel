# Написать программу для поиска в списке определённого слова
# При этом список может состоять из разного типа данных
# и иметь не ограниченное число вложенных друг в друга списков или кортежей
# поиск произвести по всем списка и кортежам, в том числе и вложенным

INPUT_LIST = [
    1, '2', 'cat', 99, 'dog',
    (4, 44, ['red', 'green', ('mother', 'father',)]),
    ['one', 'two', '55', {1, 4, 'big', True}, ['milk', 0, 'bred']],
    'End'
]


def find_word(word, input_list):
    result = False

    for item in input_list:
        if isinstance(item, str) and item == word:
            result = True
            break

        elif isinstance(item, (tuple, list)):
            result = find_word(word, item)
            if result:
                break

        elif isinstance(item, set):
            if word in item:
                if result:
                    break

    return result


def main():
    while True:
        input_word = input("Введите слово для поиска:")

        if not input_word:
            print("Ввод пуст")
            continue

        if find_word(input_word, INPUT_LIST):
            print(f"Слово {input_word} найдено")
        else:
            print(f"Слово {input_word} не найдено")

        answer = input("Хотите выйти (Y/N)")
        if answer.upper() == "Y":
            break


main()
