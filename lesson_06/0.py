# a = []
# for i in range(1, 16):
#     a.append(i)

a = [i for i in range(1, 16)]

print(a)

a1 = [2, -1, -5, 0, 5, 3]
b1 = [i**2 for i in a1]
print(b1)

a2 = {1: 10, 2: 20, 3: 30}
b2 = {i*a2[i] for i in a2}
print(b2)

b3 = [(i, a2[i]) for i in a2]
print(b3)

q = "ddj445jd 9sd 008 de344"
w = [int(i) for i in q if i.isdigit()]
print(w)

old_dict = {'aa': 1, 'b': 2, 'cccc': 3}

new_dict = {key + str(len(key)): value**2 for key, value in old_dict.items()}
new_dict_2 = {items[0] + str(len(items[0])): items[1]**2 for items in old_dict.items()}
print(new_dict)
print(new_dict_2)
