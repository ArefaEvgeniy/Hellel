japan_str = 'ぁぃえおき げず㍿ボ゛ red Арефа'
japan_char = '㍿'
color = 'red'
name = 'Tom'
surname = 'Арефа'

japan_str = japan_str.encode('utf-8')
print(japan_str)
print(type(japan_str))

japan_str = japan_str.decode()
print(japan_str)
print(type(japan_str))

print('-' * 50)

print(surname)
print(type(surname))

surname = surname.encode('utf-8')
print(surname)
print(type(surname))

surname = surname.decode('utf-16')
print(surname)
print(type(surname))
