# Написать программу для поиска файлов и построкового сравнения двух файлов.
# 1. Если код запустить с 2 аргументами, то каждым аргументом должно быть либо
# название файла, либо название файла с путём к нему, например:
# python example.py test1.txt c:\temp\test2.txt
# Данный вызов построково сравнивает текстовый файл test1.txt, который
# находится по тому же пути, что и запускаемый скрипт с текстовым файлом
# test2.txt который находится по пути: c:\temp\
# 2. Код можно запустить с ключами -f, -t и -d.
# а) Если код запускается с ключём -f то после него указывается шаблоном по
# которому в текущей директории и во всех поддиректориях будут искаться файлы.
# При этом если в имени использовать знак * - это означает любое количество любых
# символов, а знак ? - любой один символ. Пример:
# python example.py -f "*.txt"
# Данный вызов находит все файлы с расширением txt в текущей директории и всех
# поддиреториях.
# б) Скрипт можно запустить одновременно с ключом -f и ключом -t с любым текстом
# после него (если текст отделён пробелами, то его необходимо брать в кавычки).
# В этом случае будут найдены только те файлы которые соответствуют шаблону
# поиска, а так же в этих файлах должен быть указанный текст. Пример:
# python example.py -f "*.txt" -t "искомый текст"
# Данный вызов находит все файлы с расширением txt в текущей директории в которых
# есть текст "искомый текст".
# в) Так же скрипт можно запустить одновременно с ключом -f и ключом -d, после
# которого необходимо указать путь директории в которой будет осуществляться поиск
# файлов по заданному шаблону, а так же во всех её поддиректориях. Пример:
# python example.py -f "*.txt" -d "c:\user\main"
# В этом случае файлы по шаблону *.txt будут искаться в директории по пути
# c:\user\main, а так же по всех её поддиректориях.
# Если после ключа -d указать знак "/", то поиск по заданному файлов шаблону
# будет осуществляться только в текущей диретории. Пример:
# python example.py -f "*.txt" -d \
# Таким образом значение ключ -f всегда обязателен для поиска, а вот ключи -t и -d,
# при этом они могут использоваться как по одному, так и вместе в одном запросе:
# python example.py -f "*.txt" -t "искомый текст" -d \
# Чтение ключей необходимо сделать при помощи библиотеки (argparse).
# Описание библиотеки os:
# https://pythonworld.ru/moduli/modul-os.html
# https://pythonworld.ru/moduli/modul-os-path.html


import sys
import os
import re
import argparse


MES_COMPARE = "Result of compare files '{}' and '{}':"
MES_RES_COMPARE = "[{}]: {!r}  -  {!r}"
MES_SAME = "The contents of both files are the same"
MES_ERROR_FILE = "File '{}' is not exist"
MES_ERROR_ABSENT = "There is not pattern to find or start dir '{}' is absent"


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', metavar='--text', type=str, help='Needed text in file')
    parser.add_argument('-f', metavar='--file', type=str, help='Pattern of finding file')
    parser.add_argument('-d', metavar='--directory', type=str, help='Start directory to find')

    return parser.parse_args()


def read_file(file_name, read_lines=False):
    result = None
    if os.path.exists(file_name):
        with open(file_name) as f:
            if read_lines:
                result = f.readlines()
            else:
                result = f.read()
    else:
        print(MES_ERROR_FILE.format(file_name))

    return result


def compare(first_file_name, second_file_name):
    first_file = read_file(first_file_name, True)
    second_file = read_file(second_file_name, True)

    if first_file and second_file:
        print(MES_COMPARE.format(first_file_name, second_file_name))
        if len(first_file) > len(second_file):
            min_index = len(second_file)
        else:
            min_index = len(first_file)
        is_same = True

        for index in range(min_index):
            if first_file[index] != second_file[index]:
                is_same = False
                print(MES_RES_COMPARE.format(index+1, first_file[index][:75],
                                             second_file[index][:75]))
        if is_same is True:
            print(MES_SAME)


def get_file_name(find_list):
    result = None
    for index, item in enumerate(find_list):
        if os.path.isfile(item):
            result = item
            break
    else:
        if len(find_list) > 0:
            result = find_list[0]

    if result:
        find_list.remove(result)

    return find_list, result


def find_text(file, text):
    result = False
    file_data = read_file(file)
    if file_data and text in file_data:
        result = True

    return result


def find_files():
    parser = create_parser()
    subdir = False if parser.d and parser.d == '/' else True
    start_dir = parser.d if parser.d and parser.d != '/' else os.getcwd()
    text = parser.t if parser.t else None

    if parser.f is None or not os.path.isdir(start_dir):
        print(MES_ERROR_ABSENT.format(start_dir))
        return

    pattern = parser.f.replace('.', '\.').replace('+', '\+')
    pattern = pattern.replace('*', '.*').replace('?', '.?')

    join_func = lambda x: os.path.join(os.getcwd(), x)
    find_list = list(map(join_func, os.listdir(path=start_dir)))
    while True:
        find_list, file = get_file_name(find_list)
        if file is None:
            break

        if os.path.isdir(file) and subdir:
            dir_list = os.listdir(path=file)
            for item in dir_list:
                find_list.append(os.path.join(file, item))
            continue

        if re.match(pattern, os.path.split(file)[-1]):
            if text is not None:
                if find_text(file, text) is False:
                    continue
            print(file)


if __name__ == '__main__':
    if len(sys.argv) == 3 and not (sys.argv[1].startswith('-')
                                   or sys.argv[2].startswith('-')):
        compare(sys.argv[1], sys.argv[2])
    else:
        find_files()
