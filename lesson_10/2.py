# Дана переменная artist_bytes в байтовом виде.
# Декодировать её в юникод и вывести на экран.
# Декодирование значение закодировать в кодировке 'Latin1'


artist_bytes = b'Tage \xc3\x85s\xc3\xa9n'
print(artist_bytes)

artist_str = artist_bytes.decode()
print(artist_str)

artist_b_Latin = artist_str.encode('Latin1')
print(artist_b_Latin)

artist_str = artist_b_Latin.decode('Latin1')
print(artist_str)
