my_pets = ['alfred', 'rem', 'william', 'ara']
uppered_pets = []

for item in my_pets:
    uppered_pets.append(item.upper())
print(uppered_pets)


uppered_pets_2 = list(map(str.upper, my_pets))
print(uppered_pets_2)


def my_func(a):
    return a.upper()

uppered_pets_3 = list(map(my_func, my_pets))
print(uppered_pets_3)


uppered_pets_4 = list(map(lambda a: a.upper(), my_pets))
print(uppered_pets_4)
