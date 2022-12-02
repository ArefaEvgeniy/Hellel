from tkinter import *
import tkinter.messagebox as mb
import tkinter.filedialog as fd


class Entry_in():

    def __init__(self, title_in, view=SUNKEN):
        self.title_in = title_in
        self.view = view
        self.label = Label(text=self.title_in, width=0, height=3)
        self.label.pack()
        self.frm = Frame(relief=self.view, borderwidth=3, height=1)
        self.frm.pack()
        self.entry = Entry(master=self.frm, font='arial 12', width=30, justify=RIGHT)
        self.entry.pack()

    def input_panel(self):
        return self.entry


class win_inform():
    def __init__(self):
        self.btn_info = Button(text="Информационное окно")
        self.btn_warn = Button(text="Окно с предупреждением")
        self.btn_error = Button(text="Окно с ошибкой")

    def show_info(self):
        msg = "Ваши настройки сохранены"
        mb.showinfo("Информация", msg)

    def show_warning(self, text_in=''):
        msg = text_in
        mb.showwarning("Предупреждение", msg)

    def show_warning_1(self, n):
        msg = f"Добавлено записей в файл: {n}"
        mb.showwarning("Предупреждение", msg)

    def show_error(self):
        msg = "Приложение обнаружило неизвестную ошибку"
        mb.showerror("Ошибка", msg)


class File_xlsx():
    def __init__(self):
        self.btn_file = Button(text="Выбрать файл", command=self.choose_file)
        self.btn_dir = Button(text="Выбрать папку", command=self.choose_directory)
        # self.btn_file.pack(padx=60, pady=10)
        # self.btn_dir.pack(padx=60, pady=10)

    def choose_file(self):
        filetypes = (("База данных", "*.xlsx"),
                     ("Любой", "*"))
        filename = fd.askopenfilename(title="Загрузить файл", initialdir="/",
                                      filetypes=filetypes)
        if filename:
            return filename

    def choose_directory(self):
        directory = fd.askdirectory(title="Открыть папку", initialdir="/")
        if directory:
            print(directory)


class Button_p():
    def __init__(self, x, y, com_in, text_in=''):
        self.x = x
        self.y = y
        self.text_in = text_in
        self.com_in = com_in
        self.button = Button(text=self.text_in, height=1, width=10, fg="black", font='14', command=self.com_in)
        self.button.pack(side=TOP)
        self.button.place(x=self.x, y=self.y)
