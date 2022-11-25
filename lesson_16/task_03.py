# Создать свой тип данных, который у себя будет сохранять строку.
# Это будет итерируемый тип данных, но итерироваться он будет следующим образом:
# в отличии от строк которые итерируются по буквам, наш объект будет
# итерироваться по словам, при чём каждое слово он будет возвращать с заглавной
# первой буквы и с приписными остальными, в не зависимости от того в каком виде
# это слово хранится в  нашей строке. При этом точки и запятые не выводятся.


class MyIter:
    def __init__(self, value):
        self.value = value
        self.count = len(value.split())
        self.current = 0

    def __next__(self):
        if self.count > self.current:
            data = self.value.split()[self.current]
            data = data.title().strip('.').strip(',')
            self.current += 1
            return data
        raise StopIteration


class MyClass:
    def __init__(self, data):
        if isinstance(data, str):
            self.data = data
        else:
            self.data = ''
            if len(data) > 1:
                temp = []
                for item in data:
                    temp.append(str(item))
                self.data = ' '.join(temp)

    def __str__(self):
        return self.data

    def __iter__(self):
        return MyIter(self.data)


a = MyClass('Это мой КЛАСС, который имеет свой итератоР.')
b = MyClass({'red': 1, 'blue': 2, 45: 'zero'})
print(a)
print(b)

print('-' * 30)
for item in a:
    print(item)
