product_1 = 1
for item in [1, 2, 4, 8]:
    product_1 *= item
print(product_1)

print("-" * 30)

product_2 = 1
item = iter([1, 2, 4, 8])
while True:
    try:
        product_2 *= next(item)
    except StopIteration:
        break
print(product_2)
