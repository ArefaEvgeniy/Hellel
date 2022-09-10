# Написать декоратор к 2-м любым функциям, который бы считал и
# выводил время их выполнения.
# Подсказка:
# from datetime import datetime
# time = datetime.now()


from datetime import datetime
import time


def dec_time_measure(func):
    def wrapper():
        start = datetime.now()
        func()
        end = datetime.now()
        print(f"Время выполнение функции {func}: {end - start} секунд")

    return wrapper


@dec_time_measure
def test_func1():
    print("Выполняется функция testFunc1")
    time.sleep(1)
    print("Функция testFunc1 выполнена")


@dec_time_measure
def test_func2():
    print("Выполняется функция testFunc2")
    time.sleep(2)
    print("Функция testFunc2 выполнена")


test_func1()
test_func2()
