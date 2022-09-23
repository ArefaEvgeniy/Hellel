class MyIter():

    def __init__(self, value):
        self.value = value
        self.count = len(value)
        self.current = -1

    def __next__(self):
        self.current += 1
        if self.count > self.current:
            if isinstance(self.value[self.current], (int, float)):
                return abs(self.value[self.current])
            elif isinstance(self.value[self.current], str):
                if len(self.value[self.current]) > 5:
                    return f'{self.value[self.current][:5]}...'
                else:
                    return self.value[self.current]
        raise StopIteration


class MyClass():
    value = []

    def __init__(self, value):
        if not isinstance(value, list):
            value = list(value)
        for item in value:
            if isinstance(item, (int, float, str)):
                self.value.append(item)

    def __iter__(self):
        return MyIter(self.value)


a = MyClass([-1, None, -2, 4, {1: 'a', 2: 'd'}, 'ret', 'asdfghjuygtvf'])
print(a.value)
for item in a:
    print(item)
