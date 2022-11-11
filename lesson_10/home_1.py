# Дана строка в байтовом виде: b'r\xc3\xa9sum\xc3\xa9'.
# Декодировать её в строковый вид в кодировке по умолчанию.
# Затем результат преобразовать снова в байтовый, только уже в кодировке ‘Latin1’
# И на конец результат снова декодировать в строку
# (результаты всех преобразований выводить на экран).

input_data = b'r\xc3\xa9sum\xc3\xa9'
print(input_data)
data_1 = input_data.decode()
print(data_1)
data_2 = data_1.encode('Latin1')
print(data_2)
data_3 = data_2.decode('Latin1')
print(data_3)
