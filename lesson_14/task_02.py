class MyClass():

    @staticmethod
    def first_method():
        print('This is static method')

    def second_method(self):
        print('This method of object')


a = MyClass()
a.first_method()
a.second_method()

MyClass.first_method()
# MyClass.second_method()
