# Напишите функцию is_year_leap, которая принимает число (год) и возвращает True если год високосный (см. комментарий
# к слайда), False если нет.

def is_year_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


print(is_year_leap(2020))