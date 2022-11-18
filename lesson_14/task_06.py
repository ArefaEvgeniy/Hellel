class Person():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def full_name(self):
        return f'{self.name} {self.surname}'

    @full_name.setter
    def full_name(self, new):
        self.name, self.surname = new.split()

    @full_name.deleter
    def full_name(self):
        self.name, self.surname = '', ''
        print('Внимание, имя и фамилия удалены!')


person_1 = Person('Jack', 'Red')
print('name:', person_1.name)
print('surname:', person_1.surname)
print('full_name:', person_1.full_name)

print('-' * 40)

person_1.surname = 'Smith'
print('name:', person_1.name)
print('surname:', person_1.surname)
print('full_name:', person_1.full_name)
print('__dict__:', person_1.__dict__)

print('-' * 40)

person_1.full_name = 'Bob Grey'
print('name:', person_1.name)
print('surname:', person_1.surname)
print('full_name:', person_1.full_name)
print('__dict__:', person_1.__dict__)

print('-' * 40)

del(person_1.full_name)
print('name:', person_1.name)
print('surname:', person_1.surname)
print('full_name:', person_1.full_name)
print('__dict__:', person_1.__dict__)
