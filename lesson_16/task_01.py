res = 1
for i in [1, 2, 4, 8]:
	res *= i
print(res)


res = 1
i = iter([1, 2, 4, 8])
while True:
	try:
		res *= next(i)
	except StopIteration:
		break

print(res)
