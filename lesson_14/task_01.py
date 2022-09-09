class MyClass():

    @staticmethod
    def first_method():
        print("This is static method")

    def second_method(self):
        print("This is general method")


a = MyClass()
a.second_method()
a.first_method()

MyClass.first_method()
