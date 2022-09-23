from diplom.date_base import DB


def main():
    data = DB()
    call_function = {1: data.input_data, 2: data.find, 3: data.file,
                     4: data.file, 5: data.file}
    while True:
        print("1. Ввести новую запись")
        print("2. Поиск в БД")
        print("3. Загрузить данные в БД из файла")
        print("4. Сохранить данные из БД в файл")
        print("5. Экспортировать данные в json формат")
        print('-' * 50)
        print("0. Выход")
        choice = input("Ваш выбор: ")

        if not choice.isdigit() or int(choice) > 5:
            print("Не корректный ввод")
            continue
        elif int(choice) == 0:
            break

        call_function[int(choice)](int(choice))


if __name__ == "__main__":
    main()
