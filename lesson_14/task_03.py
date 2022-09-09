class Person():

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def full_name(self):
        return self.name + ' ' + self.surname

    @full_name.setter
    def full_name(self, new):
        self.name, self.surname = new.split(' ')

    @full_name.deleter
    def full_name(self):
        print("Attention!!! All been deleted!")
        self.name = ''
        self.surname = ''


a = Person('David', 'Green')
a.surname = 'Black'
print(a.name)
print(a.surname)
print(a.full_name)

print('-' * 50)

a.full_name = 'Tom Stivens'
print(a.full_name)
print(a.name)
print(a.surname)
