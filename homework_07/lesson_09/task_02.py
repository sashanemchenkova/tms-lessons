# Создайте класс Animal,
# У класса должно быть два поля:
# name, age. Все поля должны заполняться
# в конструкторе класса (метод init).

class Animal:
    def __init__(self, a_name, a_age):
        self.name = a_name
        self.age = a_age


class Dog(Animal):
    def __init__(self, a_name, a_age, d_breed):
        super().__init__(a_name, a_age)
        self.breed = d_breed


# создание объекта
my_dog = Dog('Шарик', 10, 'Доберман')

# вывод поля класса Dog
print(my_dog.breed)

# вывод полей класса, унаследованных от класса Animal
print(my_dog.name)
print(my_dog.age)
