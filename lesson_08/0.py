my_pets = ['alfred', 'rem', 'william', 'ara']
# upper_pets = []
# for pet in my_pets:
#     upper_pets.append(pet.title())
# print(upper_pets)


upper_pets = list(map(str.title, my_pets))
print(upper_pets)
