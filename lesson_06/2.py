old_dict = {'aa': 1, 'b': 2, 'cccc': 3}

new_dict = {str(key) + str(len(key)): value ** 2 for key, value in old_dict.items()}

print(new_dict)
