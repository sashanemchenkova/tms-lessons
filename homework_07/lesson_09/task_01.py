# Создайте класс Person.
# У класса должно быть три поля:
# name, surname, age.
# Все поля должны заполняться в конструкторе класса
# (метод __init__).

class Person:
    def __init__(self, u_name, u_surname, u_age):
        self.name = u_name
        self.surname = u_surname
        self.age = u_age

    #   Добавьте в класс метод get_full_name,
    #   который должен возвращать полное имя
    #   в формате "{name} {surname}"

    def get_full_name(self):
        return f' {self.name} {self.surname}'

    # Добавьте в класс метод become_older,
    # который печатает в консоль
    # "Happy birthday, {name}!"
    # и прибавляет к возрасту человека единицу.

    def become_older(self):
        self.age += 1
        print('Happy birthday,' + self.name)


# создание объекта

p = Person('Ivan', 'Ivanov', 20)

# обращение к полям класса
print(p.name)
print(p.surname)
print(p.age)
# вызов метода класса и вывод результата на экран
print(p.get_full_name())
# вызов метода класса + вывод изменившегося поля
p.become_older()
print(p.age)