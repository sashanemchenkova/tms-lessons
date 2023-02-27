# * Решите прошлую задачу, в которой теперь пользователь может вводить буквы в любом регистре.
# Вам по прежнему нужно удалить все гласные.
# При этом вывести результат нужно вывести сохранив изначальный регистр.

VOWELS = ['a', 'e', 'i', 'o', 'u']


def remove_vowels(letter_s: list[str]) -> list[str]:
    return list(filter(lambda x: x.lower() not in VOWELS,  letter_s))


letters = input('Enter : ').split()
print(remove_vowels(letters))