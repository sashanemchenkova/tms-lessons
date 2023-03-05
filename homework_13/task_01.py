# Напишите функцию is_date, которая принимает строку и возвращает bool. Функция должна вернуть True если переданная
# строка это дата в формате "DD-MM-YYYY", например "01-12-2022".


import re


def is_date(string: str) -> bool:
    return re.fullmatch(r'\d{2}-\d{2}-\d{4}', string) is not None


if __name__ == '__main__':
    assert is_date('31-08-2004')
    assert not is_date('DD-MM-YYYY')
    assert not is_date('31-MM-2004')
    assert not is_date('DD-08-2004')
    assert not is_date('31-08-Y0YY')
