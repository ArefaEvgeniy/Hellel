a_1 = {1: 'ee', 'dd': 222, 'ff': [1, 2, ('a', 'd')], 2: 'ee'}
a_2 = dict()

print(a_1)
print(type(a_1))
print(len(a_1))
print(a_2)
print(type(a_2))

print(a_1[1])
print(a_1['dd'])
print(a_1['ff'])
print(a_1['ff'][2][0])

print(1 in a_1)
print('ee' in a_1)

a_1.update({44: 555})
print(a_1)
s = a_1.pop(2)
print(a_1)
print(s)

print(a_1.keys())
print(a_1.values())
print(a_1.items())

dictionary = {'red': 'красный', 'blue': 'синий'}

print(dictionary.get('green', 'не известный'))
