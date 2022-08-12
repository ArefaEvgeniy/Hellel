# Написать программу для работы с матрицами:
# 1.Создание
# 2.Вывод
# 3.Сумма всех элементов
# 4.Нахождение максимального элемента
# 5.Нахождение минимального элемента


MATRIX = []


def create_matrix():
  result = []

  def create_line(number_of_elem):
    result = []
    counter = 0

    while counter < number_of_elem:
      value = input(f"Введите {counter}-й элемент строки матрицы: ").strip()

      if (len(value) == 1 and value.isdigit()) or \
         (len(value) > 1 and value[1:].isdigit() and
         (value[0].isdigit() or value[0] == '-')):
        result.append(int(value))
      else:
        result.append(0)

      counter += 1

    return result

  while True:
    dimension = input("Введите размерность матрицы через пробел (2 3): ")
    if dimension == '':
      dimension = '2 3'
    dimension = dimension.split()

    if len(dimension) == 2 and dimension[0].isdigit() and dimension[1].isdigit():
      if int(dimension[0]) <= 0 or int(dimension[1]) <= 0:
        print("Размерность матрицы должна быть больше 0")
        continue

      for item in range(int(dimension[0])):
        result.append(create_line(int(dimension[1])))

    else:
      print("Ошибка ввода, повторите ввод")
      continue

    break

  return result


def view_matrix():
  print(f"матрица имеет следующий вид: {str(MATRIX)}")


def sum_item_matrix():
  sum = 0

  for line in MATRIX:
    for item in line:
      sum += item

  print("Сумма элементов матрицы:", sum)


def max_item_matrix():
  max_item = None

  for line in MATRIX:
    for item in line:
      if max_item is None or item > max_item:
        max_item = item

  print("Максимальный элемент матрицы:", max_item)


def min_item_matrix():
  min_item = None

  for line in MATRIX:
    for item in line:
      if min_item is None or item < min_item:
        min_item = item

  print("Минимальный элемент матрицы:", min_item)


while True:
  if MATRIX:
    print("Выберите цифру пункта, что хотите сделать:")
    print('1.Создание')
    print('2.Вывод')
    print('3.Сумма всех элементов')
    print('4.Нахождение максимального элемента')
    print('5.Нахождение минимального элемента')
    print("0.Выход")
    print("-" * 30)
    choice = input("Сделайте ваш выбор: ")

    if not choice.isdigit() or int(choice) > 5:
      print("Ошибка ввода, повторите ввод")
      continue

    if int(choice) == 0:
      print("До свидания...")
      break
    elif int(choice) == 1:
      MATRIX = create_matrix()
    elif int(choice) == 2:
      view_matrix()
    elif int(choice) == 3:
      sum_item_matrix()
    elif int(choice) == 4:
      max_item_matrix()
    elif int(choice) == 5:
        min_item_matrix()

  else:
    MATRIX = create_matrix()
