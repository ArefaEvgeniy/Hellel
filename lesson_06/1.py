a = 10

for item in range(100, a, -5):
    print(item)


list_int = [i**2 for i in range(1, 15)]
print(list_int)


list_kub = []
for i in range(1, 15):
    list_kub.append(i**2)
print(list_int)

print("-" * 50)

first_list = ['1', 'dr', '5', '34', '-65', '5r', '0', '0.75', '102']
print(first_list)

second_list = [int(i)+2 for i in first_list if i.isdigit() and 0 < int(i) < 100]
print(second_list)
print(type(second_list))

print("-" * 50)

old_dict = {'aa': 1, 'b': 2, 'cccc': 3}
new_dict = {key + str(len(key)): value**2 for key, value in old_dict.items() if len(key) < 4}
print(new_dict)
