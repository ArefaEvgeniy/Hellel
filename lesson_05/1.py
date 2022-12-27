# Ввести предложение.
# Если в предложении есть слово code - вывести на экран "Yes, 1"
# Если в предложении есть слово codec - вывести на экран "Yes, 2"
# Иначе вывести на экран "No"

input_st = input("Input data ")

if 'codec' not in input_st:
    print("Yes, 2")
elif 'code' in input_st and len(input_st) == 4:
    print("Yes, 1")
else:
    print("No")
