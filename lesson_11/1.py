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
