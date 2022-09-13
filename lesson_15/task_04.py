class MyClass():
    name_1 = 'Class'

    def __init__(self, name):
        self.name_2 = name


a = MyClass('AAA')
b = MyClass('BBB')
c = MyClass('CCC')
print(a.name_1)
print(a.name_2)
print('-' * 30)
MyClass.name_1 = 'New Class'
print(a.name_1)
print(a.name_2)
print('-' * 30)
print(b.name_1)
print(b.name_2)
print('-' * 30)
print(c.name_1)
print(c.name_2)
print('-' * 30)
