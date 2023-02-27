# Пользователь вводит свои данные
# (имя, фамилия, возраст).
# Запишите эти данные
# в файл file_04.json формате JSON.


import json

user_name = input('enter your name : ')
user_surname = input('enter your surname : ')
user_age = input('enter your age : ')

user_dict = {'name': 'user_name',
             'surname': 'user_surname',
             'age': 'user_age',
             }

with open('task_04.json', 'w') as file:
    json.dump(user_dict, file)
