# Пользователь вводит месяц и число. Выведите True, если такой день есть в году.
a = input('enter month in english : ')
b = int(input('enter date : '))
dict_a = {
    'january': 31,
    'february': 28,
    'march': 31,
    'april': 30,
    'may': 31,
    'june': 30,
    'july': 31,
    'august': 31,
    'september': 30,
    'october': 31,
    'november': 30,
    'december': 31}
print(b <= dict_a.get(a))
