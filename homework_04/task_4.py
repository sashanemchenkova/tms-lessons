# Программа загадывает случайное число от 0 до 100. Пользователь пытается угадать, вводя числа. Если пользователь
# угадал - выведите поздравление и завершите программу. Если пользователь не угадал, подскажите ему в в какую сторону
# идти. То есть, если число пользователя слишком большое - выведите “не угадал, число больше загаданного”. Если
# меньше - выведите “не угадал, число меньше загаданного”.


import random

n = random.randint(0, 100)
while True:
    a = int(input('enter number : '))
    if a == n:
        print('congrats! ')
        break
    elif a > n:
        print('did not guess, the number is more than the guessed one ')
    elif a < n:
        print('did not guess, the number is less than the guessed one')
    else:
        print('try again ')