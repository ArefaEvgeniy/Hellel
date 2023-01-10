nums = [
    ('Jon', 15),
    ('Clarc', 12),
    ('Clarc', 7),
    ('Ban', 15),
    ('Sara', 15),
    ('Nick', 3)
]

a = nums.sort(key=lambda student: (student[1], student[0]))
print(a)
print(nums)

# a = sorted(nums, key=lambda student: (student[1], student[0]), reverse=True)
# print(a)
# print(nums)
