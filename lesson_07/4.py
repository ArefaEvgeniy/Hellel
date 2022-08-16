def area(b, h):
    return 0.5 * b * h


area_lambda = lambda b, h: 0.5 * b * h


print(area(2, 4))
print(area_lambda(2, 4))
