# Пользователь вводит одно число, сторона квардата.
# Вывести кортеж из трёх чисел: периметр квадрата, площадь квадрата, диагональ квадрата.
a = float(input('enter a - side of a square : '))
P = a * 4
S = a * a
d = a * (2 ** 0.5)
tuple_a = (P, S, d)
print(tuple_a)
