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


def find_word(word, INPUT_LIST):
    result = False

    for item in INPUT_LIST:
        if isinstance(item, (str, int)) and item == word:
            result = True
            break
        elif isinstance(item, (list, tuple)):
            result = find_word(word, item)
            if result:
                break
        elif isinstance(item, set):
            if word in item:
                result = True
                break

    return result


def main():
    input_word = input("Введите слово: ")

    if find_word(input_word, INPUT_LIST):
        print("Слово найдено")
    else:
        print("Слово не найдено")


main()
