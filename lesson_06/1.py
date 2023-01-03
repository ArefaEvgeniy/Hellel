# Дан список словарей.
# Каждый словарь описывает машину(серийный номер и год выпуска).
# Создать новый список со всеми машинами, год выпуска которых больше n.

BASE_CAR = [
    {'number': 'AE1545BB', 'year': 2020},
    {'number': 'AC5555AA', 'year': 2010},
    {'number': 'EC6674HE', 'year': 2017},
    {'number': 'BA5673OO', 'year': 2022},
    {'number': 'KA345-73', 'year': 2000},
    {'number': 'CA576-28', 'year': 1993}
]

n = 2020

list_car = [(i['number'], i['year']) for i in BASE_CAR if i['year'] >= n]

print(list_car)
