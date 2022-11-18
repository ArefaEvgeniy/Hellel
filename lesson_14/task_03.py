class A():
    class_atr = 10

    def __init__(self, attr=0):
        self.attr = attr


object_1 = A(1)
print('A.class_atr:', A.class_atr)
print('object_1.class_atr:', object_1.class_atr)
print('object_1.attr:', object_1.attr)
print('dict object_1:', object_1.__dict__)

object_2 = A(5)
print('A.class_atr:', A.class_atr)
print('object_2.class_atr:', object_2.class_atr)
print('object_2.attr:', object_2.attr)
print('dict object_2:', object_2.__dict__)

A.class_atr += 2
print('-' * 30)

print('A.class_atr:', A.class_atr)
print('object_1.class_atr:', object_1.class_atr)
print('dict object_1:', object_1.__dict__)
print('object_2.class_atr:', object_2.class_atr)
print('dict object_2:', object_2.__dict__)

object_1.class_atr = 15
object_1.sss = 101
print('-' * 30)

print('A.class_atr:', A.class_atr)
print('object_1.class_atr:', object_1.class_atr)
print('dict object_1:', object_1.__dict__)
print('object_2.class_atr:', object_2.class_atr)
print('dict object_2:', object_2.__dict__)
