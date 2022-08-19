my_pets = ['alfred', 'rem', 'william', 'ara']

up_my_pets = []
for pet in my_pets:
    up_my_pets.append(pet.title())
print(up_my_pets)

up_2_my_pets = list(map(str.title, my_pets))
print(up_2_my_pets)

up_3_my_pets = list(map(lambda x: x.title(), my_pets))
print(up_3_my_pets)

aa = lambda x: x.title()

print(aa('eertt'))
