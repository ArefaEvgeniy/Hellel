nums = [
    ('Jon', 15),
    ('Clorc', 12),
    ('Clarc', 7),
    ('Ban', 15),
    ('Sara', 15),
    ('Nick', 3)
]


print(sorted(nums))
print(sorted(nums, key=lambda student: (student[1], student[0])))
print(list(map(lambda x: (x[1], x[0]), sorted(nums, key=lambda student: (student[1], student[0])))))
