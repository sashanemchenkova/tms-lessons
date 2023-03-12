import sqlite3


def alfabet_order():
    with sqlite3.connect('/home/admin/tms-lessons/homework_14/telephone.py.db') as connection:
        result_2 = connection.execute(
            'SELECT * FROM my_phone ORDER BY name'
        )
        print(result_2.fetchall())


def new_kontakt(new_name, new_tel_number):
    with sqlite3.connect('/home/admin/tms-lessons/homework_14/telephone.py.db') as connection:
        result_1 = connection.execute(
            f'INSERT INTO my_phone(name, tel_number) VALUES (?, ? ) ',
            (new_name, new_tel_number)
        )
        print(result_1.fetchall())


while True:
    print('')
    print('0. Выйти из программы')
    print('1. Добавить новый контакт')
    print('2. Вывести весь список контактов в алфавитном порядке')
    print('3. Обновить номер контакта')
    action = int(input())
    if action == 0:
        break
    elif action == 2:
        alfabet_order()
    elif action == 1:
        new_name = input('Имя : ')
        new_tel_number = int(input('Телефон : '))
        new_kontakt(new_name, new_tel_number)
        print('Контакт добавлен')
