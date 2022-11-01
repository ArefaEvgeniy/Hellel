data = b'ci\xc3\xa0o'

with open('test.txt', 'w', encoding='Latin1') as f:
    f.write(data.decode())

try:
    f = open('test.txt', encoding='Latin1')
    print(f.read())
finally:
    f.close()
