# Написать программу для работы с данными о людях.
# Программа должна уметь загружать данные из файла, сохранять в файл, вводить новые записи и производить поиск
# по существующим записям.
# Программа сохраняет данные о человеке, а именно: ФИО, дата рождения, дата смерти (может отсутствовать) и пол.
# При этом ФИО вводится 3 полями: Имя (обязательно), Фамилия и Отчество могут не вводится.
# Программа должна уметь вычислять возраст человека (количество полных лет) на основании даты рождения и
# даты смерти или сегодняшней даты, если дата смерти отсутствует.
# Дата рождения и дата смерти может вводится в формате:
# 12.10.1980
# 11 10 2000
# 01/02/1995
# 3-9-2007
# Поиск может производится по имени, фамилии и отчеству и выдаёт все варианты, которые подходят под строку поиска
# (это может быть имя, или фамилия, или имя и фамилия, или только часть имени и т.д.).
# К примеру, есть такие записи:
# Евгений Крут Михайлович, 12.10.1980, 11.10.2001, m
# Евгения, 12.10.1980, 12.10.2001, f
# Дмитрий Евгеньевич, 10.03.2000, m
# При поиске "евген", выдаются такие данные:
# Евгений Крут Михайлович  20 лет, мужчина. Родился: 12.10.1980. Умер: 11.10.2001.
# Евгения 21 год, женщина. Родилась: 12.10.1980. Умерла: 12.10.2001.
# Дмитрий Евгеньевич 22 года, мужчина. Родился: 10.03.2000.
# Программа при старте начинает работать с пустой базой данных. Оператор может заполнять её, а может при желании
# загрузить ранее сохранённые данные из файла (желательно Excel).
#
# Когда есть какие-то записи оператор может сохранить их в файл введя его название.

# Желательная структура программы:

# в основной части программы находится вечный цикл с меню, что может выбрать оператор;
# сами данные организованы в виде класса в другом файле, который импортируется в файл основной части программы,
# где создаётся объект соответствующего класса перед заходом в вечный цикл;
# все пункты меню основной части программы вызывают те или иные методы у созданного объекта данных;
# при желании можно в третьем файле создать отдельный класс Person который будет импортироваться в файл с данными.
# Именно в этом классе будет происходить валидация введённых данных.
#
#
# *Все перечисленные описания являются пожеланиями по реализации дипломного проекта и в силу тех или иных причин
# могут быть изменены по желанию студента. Основные требования:
#
# программа позволяет ввести новые данные о людях;
# производить поиск по уже введённым данным;
# правильно рассчитывать количество полных лет человека на основе даты рождения и даты смерти или текущей даты.

from functions import *
from fun_tkinter import *
from tkinter import *
import re
import os
import sys
import os.path


root = Tk()
root.title('Жильцы микрорайона Победа')
root.resizable = (False, False) # запрет на изменение размеров окна
# root.geometry("400x550+1400+350")
root.geometry("400x550+50+250")



ent_last_name = Entry_in("Фамилия*")
ent_first_name = Entry_in("Имя")
ent_patr = Entry_in("Отчество")
ent_date_birth = Entry_in("Дата рождения*")
ent_date_death = Entry_in("Дата смерти")
ent_sex = Entry_in("Пол* (муж*, жен*, f*, m*)")
save_file = File_xlsx()


def file_save():
    try:
        path_file = File_xlsx()
        path = path_file.choose_file()
        amount = insert_in_db(path)
        win = win_inform()
        win.show_warning_1(amount)
    except:
        x_t = win_inform()
        x_t.show_warning("Не удалось загрузить данные из файла")


def db_inpanel():
    panel_massiv = []
    in_l = ent_last_name.input_panel().get()
    in_f = ent_first_name.input_panel().get()
    in_p = ent_patr.input_panel().get()
    in_b = ent_date_birth.input_panel().get()
    in_d = ent_date_death.input_panel().get()
    in_s = ent_sex.input_panel().get()
    if in_l and in_b and in_s:
        in_l = check_string(in_l)
        in_f = check_string(in_f)
        in_p = check_string(in_p)
        in_b = re.findall(KEY_DATA, in_b)
        if in_b:
            in_b = convert_data(in_b[0])
        in_d = re.findall(KEY_DATA, in_d)
        if in_d:
            in_d = convert_data(in_d[0])
        if in_d and in_b and in_b > in_d:
            in_b = None
            x_t = win_inform()
            x_t.show_warning("Дата смерти раньше даты рождения")
            ent_date_birth.input_panel().delete('0', END)
            ent_date_death.input_panel().delete('0', END)
        if in_s:
            in_s = check_sex(in_s)
        if in_l and in_b and in_s:
            if not in_f:
                in_f = None
            if not in_p:
                in_p = None
            if not in_d:
                in_d = None
            panel_massiv.append((in_l, in_f, in_p, in_b, in_d, in_s))
            add_file_db(panel_massiv)

            ent_last_name.input_panel().delete('0', END)
            ent_first_name.input_panel().delete('0', END)
            ent_patr.input_panel().delete('0', END)
            ent_date_birth.input_panel().delete('0', END)
            ent_date_death.input_panel().delete('0', END)
            ent_sex.input_panel().delete('0', END)
            x_t = win_inform()
            x_t.show_warning("Данные загружены в БД")
        else:
            x_t = win_inform()
            x_t.show_warning("Не заполнены все поля или формат ввода не корректный")
    else:
        x_t = win_inform()
        x_t.show_warning("Не заполнены все поля или формат ввода не корректный")


# вывод данных из БД в файл
def search_in_sql(list=''):
    try:
        search_list = db_check_out(list)
    except:
        x_d = win_inform()
        x_d.show_warning("БД не создана")
        return
    if not search_list:
        x_t = win_inform()
        x_t.show_warning("Записи в БД не найдены")
    else:
        with open("reviev.txt", "w") as file_txt:
            for string in search_list:
                print(preparation(string), file=file_txt)
        file_txt.close()
        path_txt = os.path.join(sys.path[0], "reviev.txt")
        os.startfile(path_txt)


# нажатие кнопки "Искать"
def button_e():
    if ent_scan.get():
        search_in_sql(ent_scan.get())
        ent_scan.delete('0', END)


# окно поиска по шаблону
def win_s():
    win = Toplevel(root,  bd=10, bg="lightblue")
    win.title("Окно поиска")
    win.geometry("350x100+500+550")

    frm = Frame(win, relief=SUNKEN, borderwidth=5, height=1)
    frm.pack()
    global ent_scan
    ent_scan = Entry(master=frm, font='arial 14', width=30, justify=RIGHT)
    ent_scan.pack()

    button = Button(win, text="Искать", height=1, width=10, fg="black", font='14', command=button_e)
    button.pack(side=TOP)
    button.place(x=120, y=50)


# окно поиска по дате
def win_d():
    win = Toplevel(root,  bd=10, bg="lightblue")
    win.title("Окно поиска по дате")
    win.geometry("350x200+500+550")

    label = Label(win, text="Диапазон должен быть в формате: \n 'от  до' (5  25) или 'до' (47)",
                  width=0, height=5, bg="lightblue")
    label.pack()

    frm = Frame(win, relief=SUNKEN, borderwidth=5, height=1)
    frm.pack()
    global ent_o_scan
    ent_o_scan = Entry(master=frm, font='arial 14', width=30, justify=RIGHT)
    ent_o_scan.pack()

    button = Button(win, text="Искать", height=1, width=10, fg="black", font='14', command=button_o)
    button.pack(side=TOP)
    button.place(x=120, y=145)


def outgoing(massiv, end, start=0):
    data_old = []
    for item in massiv:
        data = datetime.datetime.strptime(item[4], "%Y-%m-%d").date()
        now_ = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d")
        now = datetime.datetime.strptime(now_, "%Y-%m-%d").date()
        diff = (now - data)
        if int(diff.days)//365 in range(start, end+1):
            list(item).pop(0)
            data_old.append(tuple(item))
    if not data_old:
        x_t = win_inform()
        x_t.show_warning("Записи в БД не найдены")
    else:
        with open("reviev.txt", "w") as file_txt:
            for string in data_old:
                print(preparation(string), file=file_txt)
        file_txt.close()
        path_txt = os.path.join(sys.path[0], "reviev.txt")
        os.startfile(path_txt)


def button_o():
    try:
        data_old = search_alive()
    except:
        x_d = win_inform()
        x_d.show_warning("БД не создана")
        return

    x = ent_o_scan.get().split()
    if x and len(x) == 1 and x[0].isdigit() and float(x[0]) in range(101):
        end = int(float(x[0]))
        outgoing(data_old, end)
    elif x and len(x) == 2 and x[0].isdigit() and float(x[0]) in range(101) and x[1].isdigit() and float(x[1])\
        in range(101) and float(x[0]) < float(x[1]):
        start = int(float(x[0]))
        end = int(float(x[1]))
        outgoing(data_old, end, start)
    else:
        x_d = win_inform()
        x_d.show_warning("Не правильный формат ввода")
    ent_o_scan.delete('0', END)


btn_1 = Button_p(150, 500, db_inpanel, "Ввод в БД")


# создание меню
menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
search_menu = Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить из файла", command=file_save)

menu_bar.add_cascade(label="Поиск", menu=search_menu)
search_menu.add_command(label="Поиск по шаблону", command=win_s)
search_menu.add_command(label="Поиск по возрасту (start, end)", command=win_d)
search_menu.add_command(label="Вывести всю БД", command=search_in_sql)
search_menu.add_command(label="Список умерших", command=death)
search_menu.add_command(label="Список живых", command=alive)
search_menu.add_command(label="Список женщин", command=women)
search_menu.add_command(label="Список мужчин", command=men)
search_menu.add_command(label="Список совершеннолетних", command=adult)

root.config(menu=menu_bar)


root.mainloop()
