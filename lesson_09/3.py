nums_1 = [2, 5, -40, 12, 456, 23, 1, 0]
nums_2 = [2, 5, -40, 12, 456, 23, 1, 0]

num_3 = sorted(list(filter(lambda x: x > 1, nums_1)), reverse=True)
print(num_3)
print(nums_1)
print('-' * 50)
print(nums_2.sort(reverse=True))
print(nums_2)
