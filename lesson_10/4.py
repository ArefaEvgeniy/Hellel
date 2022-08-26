data = b'ci\xc3\xa0o'


with open('task.txt', 'w', encoding='Latin1') as f:
    f.write(data.decode('Latin1'))


try:
    f = open('task.txt')
    word = f.read()
    print(word)
    print(type(word))
finally:
    f.close()
