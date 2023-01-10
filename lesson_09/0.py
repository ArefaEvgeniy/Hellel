list_data = [1, 3, 5, 2, 3, 'er', 5, 'er', 't', 3, 5, 0]

def func(data):
    dict_data = {}
    for item in data:
        if dict_data.get(item):
            dict_data[item] += 1
        else:
            dict_data.update({item: 1})

func(list_data)
