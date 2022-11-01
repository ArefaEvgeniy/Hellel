text = 'Text'
text_2 = 'Text\ntext2\ttext3'
number = 3.14159

print(text)
print('{:<30}'.format(text))
print('{:>30}'.format(text))
print('{:^30}'.format(text))
print(f'{text:-^30}')

print('{}'.format(text_2))
print('{!r}'.format(text_2))

print('{}'.format(number))
print(f'{number:.3f}')
