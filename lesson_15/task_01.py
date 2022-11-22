# text = 'Евгений'
text = 1
# text = 'Bob'

try:
    text_encode = text.encode('Latin-1')
except UnicodeEncodeError as error:
    print('Wrong encode:', error)
    text_encode = text.encode()
except AttributeError as error:
    print('AttributeError:', error)
    text_encode = ''
except (NameError, EOFError, IndexError) as error:
    print('NameError:', error)
    text_encode = None
except Exception as error:
    print('--- Exception ----', error)
    text_encode = None
else:
    print('ELSE')
finally:
    print('FINALLY')

print('text:', text_encode)
print('type:', type(text_encode))


try:
    ...
finally:
    ...
