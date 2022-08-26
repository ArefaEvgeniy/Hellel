# Дана переменная artist_bytes в байтовом виде.
# Декодировать её в юникод и вывести на экран.
# Декодирование значение закодировать в кодировке 'Latin1'


artist_bytes = b'Tage \xc3\x85s\xc3\xa9n'
artist_str = artist_bytes.decode()
print(artist_bytes)
print(artist_str)

artist_latin1 = artist_str.encode('Latin1')
print(artist_latin1)
artist_latin1_str = artist_latin1.decode('Latin1')
print(artist_latin1_str)

