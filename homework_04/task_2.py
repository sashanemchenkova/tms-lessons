# Программа выводит на экран числа от 0 до 100.
# После вывода каждого числа спрашивайте у пользователя “Should we break?”.
# Если он ответил “yes” - завершите программу.
# Иначе - продолжайте вывод чисел.


for i in range(0, 101):
    print(i)
    answer = input('should we break? ')
    if answer == 'no':
        i += 1
    else:
        break