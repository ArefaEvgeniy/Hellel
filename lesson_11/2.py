# Записать в CSV-файл нижеприведённые данные.
# После этого прочитать этот файл и вывести данные в виде таблицы


import csv

name_of_fields = ["Name", "Class", "Age"]
field_01 = ["Jan", "3", "10"]
field_02 = ["Alex", "5", "12"]
field_03 = ["Michael", "11", "18"]


with open('task_02.csv', 'w', encoding='utf-8') as f:
    file_writer = csv.writer(f)
    for item in (name_of_fields, field_01, field_02, field_03):
        file_writer.writerow(item)

with open('task_03.csv', encoding='utf-8') as f:
    file_reader = csv.reader(f)
    counter = 0
    for item in file_reader:
        print(f'{item[0]}  |  {item[1]}    |    {item[2]}   |     {item[3]} ')
        if counter == 0:
            name_of_columns = item
        counter += 1

print(name_of_columns)
