# Создайте класс Person.
# У класса должно быть три поля: full_name, age, gender, которые должны заполняться в конструкторе.
# Будем считать что поле gender имеет тип str и может быть либо 'M' (male), либо 'F' (female).


class Person:
    def __init__(self, full_name, age, gender):
        self.full_name = full_name
        self.age = age
        self.gender = gender

    # Добавьте в класс метод print_person_info, который печатает на экран строку:
    # "Person: {full_name} ({gender}), {age} years old"

    def print_person_info(self):
        print(f'Person : {self.full_name} ({self.gender}), {self.age} years old')

    def get_birth_year(self):
        return 2023 - self.age