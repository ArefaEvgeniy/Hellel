# Сериализовать словарь в json-формат и сохранить сериализованные
# данные в файл. А также в строковый формат без сохранения в файл.
# Десириализовать записанные данные с диска.


import json

input_data = [
  {
    'userId': 1,
    "id": 1,
    "score": 5000.45,
    "name": 'Tom',
    'completed': False
  },
  {
    "userId": 34,
    'id': 2,
    "score": 2.003,
    "name": "Sam",
    'completed': True
  },
]


with open('task_01.json', 'w') as f:
    json.dump(input_data, f)


with open('task_01.json') as f:
    output_data = json.load(f)


with open('task_01.json') as f:
    output_data_2 = f.read()


print(output_data)
print(type(output_data))

print(output_data_2)
print(type(output_data_2))

file_data = json.dumps(input_data)

print(file_data)
print(type(file_data))

file_data_2 = json.loads(file_data)

print(file_data_2)
print(type(file_data_2))
