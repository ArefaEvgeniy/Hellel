# Записать в CSV-файл нижеприведённые данные.
# После этого прочитать этот файл и вывести данные в виде таблицы


import csv

name_of_filds = ['Name', 'Grade', 'Age']
field_01 = ['Jack', '3', '10']
field_02 = ['Tom', '5', '12']
field_03 = ['Sam', '11', '18']


with open('task_02.csv', mode='w', encoding='utf-8') as f:
    file_writer = csv.writer(f)
    for item in (name_of_filds, field_01, field_02, field_03):
        file_writer.writerow(item)

print('-' * 50)

with open('task_02.csv', encoding='utf-8') as f:
    file_reader = csv.reader(f)
    count = 0
    for row in file_reader:
        print(f'{row[0]} | {row[1]} | {row[2]}')
        if count == 0:
            print('-' * 20)
        count += 1
