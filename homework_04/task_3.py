# Сделайте предыдущую задачу, добавив проверку на корректность ответа пользователя. Если он ответил “yes” - завершите
# программу. Если он ответил “no” - продолжайте - продолжайте вывод чисел. Если что-то другое - напечатайте "Don't
# understand you" и продолжайте спрашивать до тех пор, пока ответ не будет корректным.


for i in range(0, 101, 1):

    answer = input('should we break? ')
    if answer == 'no':
        print(i)
        i += 1
    elif answer == 'yes':
        break
    else:
        print('do not understand you, try again ')
        print(i)
