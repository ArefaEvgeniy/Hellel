class MyClass():
    TOTAL_OBJECTS = 0

    def __init__(self):
        MyClass.TOTAL_OBJECTS += 1

    @classmethod
    def total_objects(cls):
        print('Total objects:', cls.TOTAL_OBJECTS)


obj_1 = MyClass()
obj_2 = MyClass()
obj_3 = MyClass()
obj_4 = MyClass()
obj_5 = MyClass()
obj_6 = MyClass()
obj_7 = MyClass()
obj_10 = MyClass()

obj_1.total_objects()
obj_7.total_objects()
MyClass.total_objects()
