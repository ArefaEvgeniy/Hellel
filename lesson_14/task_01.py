class MyList(list):
    def __init__(self, data):
        for item in data:
            if item not in self and isinstance(item, (int, str)):
                self.append(item)

    def __add__(self, other):
        ...

    def __sub__(self, other):
        data = self[:]
        for item in other:
            if item in data:
                data.remove(item)
        return MyList(data)


a = MyList((1, 2, 5, 3, 4, 5, 'f', 'd', 2, 'e'))   # [1, 2, 5, 3, 4, 'f', 'd', 'e']
b = MyList((3, 5, 'e', 'e', 9))   # [3, 5, 'e', 9]

e = a + b
c = a - b   # [1, 2, 4, 'f', 'd']

print('e:', e)
print('c:', c)
print('type:', type(c))
