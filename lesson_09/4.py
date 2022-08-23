in_list = (
    ('Jon', 14),
    ('Kati', 6),
    ('Jon S', 14),
    ('Clarc', 20),
    ('Nick', 9),
    ('Sara', 3),
    ('Sara', 9),
    ('Jack', 9),
)

print(sorted(in_list))
print(sorted(in_list, key=lambda x: x[1]))
print(sorted(in_list, key=lambda x: (x[1], x[0])))

sum_func = lambda num: (lambda x, y, z: x + y + z)(*num)

print(sum_func((3, 5, 6)))
