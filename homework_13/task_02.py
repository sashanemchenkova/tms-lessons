# Напишите функцию is_float_number, которая принимает строку и возвращает bool. Функция должна вернуть True если
# переданная строка это корректное число с плавающей точкой. Например "1.0", "20.45".

import re


def is_float_number(string: str) -> bool:
    return re.fullmatch(r'\d+[.]\d+', string) is not None


if __name__ == '__main__':
    assert is_float_number('10.0')
    assert is_float_number('0.01')
    assert is_float_number('20.45')
    assert not is_float_number('d.01')
    assert not is_float_number('d.d')
    assert not is_float_number('12.s')
    assert not is_float_number('12!5')


