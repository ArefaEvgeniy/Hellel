from datetime import datetime


class Person(object):

    def __init__(self, name, s_name, l_name, birthday, death, sex):
        self.name = name.title()
        self.s_name = s_name.title()
        self.l_name = l_name.title()
        self.birthday = birthday
        self.death = death
        self.sex = sex.lower()
        self.error = ""
        self.age = "0"

    def __str__(self):
        sex = "мужчина" if self.sex == "m" else "женщина"
        birth = "Родился: " if self.sex == "m" else "Родилась: "
        birth += str(self.birthday)
        if self.death:
            death = "Умер: " if self.sex == "m" else "Умерла: "
            death += str(self.death) + ". "
        else:
            death = ""
        return f"{self.full_name} {self.print_age}, {sex}. {birth}. {death}".strip()

    @property
    def full_name(self):
        return f"{self.name} {self.s_name} {self.l_name}".strip()

    @property
    def print_age(self):
        prefix = "лет"
        if int(self.age[-1]) == 1:
            prefix = "год"
        elif int(self.age[-1]) < 5 and \
                not (len(self.age) > 1 and int(self.age[-2]) == 1):
            prefix = "года"
        return f"{self.age} {prefix}"

    @staticmethod
    def valid_date(date):
        result = None
        date = date.replace(',', '.').replace('/', '.').replace('\\', '.')
        date = date.replace('-', '.').replace('  ', '.').replace(' ', '.')
        date = date.split('.')
        if len(date) == 3:
            try:
                date = datetime(int(date[2]), int(date[1]), int(date[0]))
                result = date.strftime("%d.%m.%Y")
            except Exception:
                pass
        return result

    def __calculate_age(self):
        birthday = self.birthday.split('.')

        death = self.death if self.death else datetime.now().strftime("%d.%m.%Y")
        death = death.split('.')

        if int(death[0]) - int(birthday[0]) < 0:
            death[1] = int(death[1]) - 1
        self.age = str(int(death[2]) - int(birthday[2]))
        if int(death[1]) - int(birthday[1]) < 0:
            self.age = str(int(self.age) - 1)

    def valid(self):
        if not self.name:
            self.error = "Вы не ввели имя"
            return False

        if self.sex not in ('m', 'f'):
            self.error = "Ошибка ввода пола"
            return False

        birthday = self.valid_date(self.birthday)
        if birthday is None:
            self.error = "Ошибка при вводе даты рождения"
            return False
        else:
            self.birthday = birthday

        death = self.valid_date(self.death) if self.death else ''
        if death is None:
            self.error = "Ошибка при вводе даты смерти"
            return False
        else:
            self.death = death

        self.__calculate_age()
        if int(self.age) < 0:
            self.error = "Возраст не может быть отрицательным"
            return False

        return True
