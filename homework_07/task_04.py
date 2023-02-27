# Пользователь вводит произвольное количество слов через пробел.
# Затем (на следующей строке) вводит один символ (разделитель).
# Вам нужно написать функцию my_join, которая принимает список из строк и символ-разделить,
# и возвращает строку, в которой все слова из списка соединены через символ разделитель.
#
# Пример ввода пользователя:
# hello this is my string
# @
#
# Вывод программы: hello@this@is@my@string

from functools import reduce


def my_join(list_u: list[str], separator: str) -> str:
    return reduce(lambda x, y: x + separator + y, list_u)


user_list = input('Enter : ').split()
sep = input('Separator : ')

print(my_join(user_list, sep))