# Сериализовать словарь в json-формат и сохранить сериализованные
# данные в файл. А также в строковый формат без сохранения в файл.
# Десириализовать записанные данные с диска.


import json

input_data = [
  {
    "userId": 1,
    "id": 1,
    "score": 5000.45,
    "name": "Tom",
    "completed": False
  },
  {
    "userId": 34,
    "id": 2,
    "score": 2.003,
    "name": "Sam",
    "completed": True,
    "children": (
      {
        "firstName": "Alice",
        "age": 12
      },
      {
        "firstName": "Bob",
        "age": 8
      }
    )
  },
]


with open('task_01.json', 'w') as f:
  json.dump(input_data, f)


with open('task_01.json') as f:
  output_data = json.load(f)

print('output_data:\n', output_data)
print('type:', type(output_data))

print('-' * 50)

input_data2 = json.dumps(input_data)
print('input_data2:\n', input_data2)
print('type:', type(input_data2))
