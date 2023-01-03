name_list = ['Bob', 'KATE', 'jack']

my_func = lambda a: [f'Hello, {name.title()}' for name in a]

print(my_func(name_list))

new_list = ['ДИМА', 'ЛЕНА', 'Катя']

print(my_func(new_list))
