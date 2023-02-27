# Создайте словарь с вашими данными
# (имя, фамилия, и т.д),
# запишите его в файл file_03.json в формате JSON.


import json

data = {'name': 'Alexandra', 'surname': 'Nemchenkova'}

with open('file_03.json', 'w') as file:
    json.dump(data, file)
