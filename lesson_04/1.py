a = 5
b = "text"
print("Вывод 1", "Вывод 2", a, b, sep=": ")

print("а разделить на 100, будет: ", a, sep="0.0", end="\n\n\n")

source_file = open("python.txt", "a")

print("Hello, world", file=source_file, end="")
source_file.close()

c = input("Введите ваше имя: ").upper().title().split()
print("Hello,", c)

d1 = int(input("Введите первое слогаемое: "))
d2 = int(input("Введите второе слогаемое: "))
print("Сумма:", d1 + d2)
