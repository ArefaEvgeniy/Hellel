# Написать программу аналог команды top или htop для Linux-систем.
# Программу написать на основе данных полученных из утилиты psutil.
# Вывод необходимо сделать по возможности красивым и максимально
# приближенным к выводу команд top или htop.
# В начале необходимо в графическом виде и виде процентов вывести информацию
# о частоте и загрузке процессоре, а атк же о памяти: используемая/доступная.
# После этого необходимо в табличном виде вывести информацию о первых 30 -
# 35 процессах разбитой по столбцам: pid, username, cpu, memory, time, command.
# В каждой новой строке информация о новом процессе, на подобии как в top.
# Желательно, чтобы как по аналогии с командами top или htop информация
# постоянно обновлялась, где-то через каждые 2-3 секунды.
# Предусмотреть возможность сортировки процессов по любому из параметров.
# Как вариант, это можно сделать при помощи аргументов при запуске скрипта (argparse).
# Ссылка как вывод сделать цветным: https://egorovegor.ru/python-color-printing/


import argparse
import psutil
import os
import time

import const

from datetime import datetime
from collections import namedtuple


key_sort = {
    const.PID: lambda x: x.pid,
    const.USERNAME: lambda x: x.username,
    const.CPU: lambda x: x.cpu,
    const.MEMORY: lambda x: x.mem,
    const.TIME: lambda x: x.time,
    const.COMMAND: lambda x: x.command,
}
named_pids = namedtuple(
    'named_pids', f'{const.PID} {const.USERNAME} {const.CPU} {const.MEMORY} '
                  f'{const.TIME} {const.COMMAND}'
)


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', metavar='--sort', type=str, help='Name of item for sort')
    parser.add_argument('-r', metavar='--reverse', type=str, help='Reversed sort')

    return parser.parse_args()


def convert_bytes(value):
    if value < 1024 * 1024:
        divider, suffix = 1024, 'Kb'
    elif value < 1024 * 1024 * 1024:
        divider, suffix = 1024 * 1024, 'Mb'
    elif value < 1024 * 1024 * 1024 * 1024:
        divider, suffix = 1024 * 1024 * 1024, 'Gb'
    else:
        divider, suffix = 1024 * 1024 * 1024 * 1024, 'Tb'

    return f'{round(value/divider, 2)}{suffix}'


def get_processes():
    result = []
    list_pids = psutil.pids()
    new_list = []

    for index, item in enumerate(list_pids):
        try:
            pid = psutil.Process(item)
        except psutil.NoSuchProcess:
            continue
        pid.cpu_percent()
        new_list.append((item, pid))

    time.sleep(1)

    for item in new_list:
        try:
            result.append(named_pids(
                item[0],
                item[1].username(),
                item[1].cpu_percent(),
                round(item[1].memory_percent(), 1),
                datetime.fromtimestamp(item[1].create_time())
                .strftime(const.TIME_FORMAT),
                item[1].name())
            )
        except psutil.NoSuchProcess:
            continue

    return result


def get_cpu():
    freq_min = psutil.cpu_freq().min
    freq_cur = psutil.cpu_freq().current
    freq_max = psutil.cpu_freq().max
    freq = round(((freq_cur - freq_min) / (freq_max - freq_min)) * 100, 2)
    percent = psutil.cpu_percent(interval=1)

    return freq, percent


def get_memory():
    total = convert_bytes(psutil.virtual_memory().total)
    used = convert_bytes(psutil.virtual_memory().used)
    percent = psutil.virtual_memory().percent

    return total, used, percent


def print_percent(prefix, percent, suffix):
    print(f'{const.TEXT_BLUE}{prefix.title():>4}', sep='', end='')
    print(f'{const.TEXT_WHITE}[', sep='', end='')
    for i in range(1, 101):
        color = const.TEXT_GREEN
        if i > 50:
            color = const.TEXT_YELLOW if i < 80 else const.TEXT_RED
        if percent > i:
            print(f'{color}|', sep='', end='')
        else:
            print(' ', sep='', end='')
    print(f'{const.TEXT_WHITE}]', end='')
    print(f'{const.TEXT_GRAY}{suffix}{const.FONT_CANCEL}')


def print_info(pids, cpu, memory, font):
    os.system('clear')

    font_1 = const.FONT_BLUE if font == const.PID else const.FONT_GREEN
    font_2 = const.FONT_BLUE if font == const.USERNAME else const.FONT_GREEN
    font_3 = const.FONT_BLUE if font == const.CPU else const.FONT_GREEN
    font_4 = const.FONT_BLUE if font == const.MEMORY else const.FONT_GREEN
    font_5 = const.FONT_BLUE if font == const.TIME else const.FONT_GREEN
    font_6 = const.FONT_BLUE if font == const.COMMAND else const.FONT_GREEN

    print_percent(f'{const.FREQ}', cpu[0], f'{cpu[0]}%')
    print_percent(f'{const.CPU}', cpu[1], f'{cpu[1]}%')
    print_percent(f'{const.MEMORY}', memory[2], f'{memory[1]}/{memory[0]}')

    print(
        f'{font_1}  {const.PID.upper()}  {font_2}    {const.USERNAME.upper()} '
        f'   {font_3}  {const.CPU.upper()}% {font_4}  {const.MEMORY.upper()}% '
        f'{font_5}   {const.TIME.upper()}   {font_6} {const.COMMAND.upper()}  '
        f'{const.FONT_CANCEL}'
    )

    for index, item in enumerate(pids):
        if index > 35:
            break
        print(f'{item.pid:>5}  {item.username[:12]:<12} {item.cpu:>9} {item.mem:>6} {item.time:>9}  {item.command}')


def main():
    parser = create_parser()
    sorted_key = key_sort.get(parser.s, key_sort[const.PID])

    while True:
        pids = get_processes()
        pids.sort(key=sorted_key, reverse=True if parser.r else False)
        cpu = get_cpu()
        memory = get_memory()
        print_info(pids, cpu, memory, create_parser().s)


if __name__ == '__main__':
    main()

