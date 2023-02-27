# Пользователь вводит произвольное количество маленьких латинских букв через пробел.
# Напишите функцию remove_vowels, которая принимает список из этих букв и удаляет из него все гласные буквы.
# Выведите результат работы на экран.
#
# Пример:
# Ввод пользователя: a b c d e f
# Результат программы: ['b', 'c', 'd', 'f']

VOWELS = ['a', 'e', 'i', 'o', 'u']


def remove_vowels(letter_s: list[str]) -> list[str]:
    return list(filter(lambda x: x not in VOWELS, letter_s))


letters = input('Enter : ').split()
print(remove_vowels(letters))