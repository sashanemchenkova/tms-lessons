# Пользователь вводит произвольную строку. Выведите кортеж из уникальных символов введённой строки.
a = str(input('enter string : '))

print(tuple(set(a)))