class Animal:
    def __init__(self, a_name, a_age):
        self.name = a_name
        self.age = a_age

    def make_voice(self):
        print('Я не знаю какой звук мне издать,я же абстрактное животное')


class Dog(Animal):
    def __init__(self, a_name, a_age, d_breed):
        super().__init__(a_name, a_age)
        self.breed = d_breed

    def make_voice(self):
        print('Гав')


class Cat(Animal):
    def __init__(self, a_name, a_age, cat_is_vaccinated):
        super().__init__(a_name, a_age)
        self.is_vaccinated = cat_is_vaccinated

    def make_voice(self):
        print('Мяу')


animals = [
    Animal('Животное', 5),  # создание абстрактного животного довольно бессмысленно, но для понимания ООП это ок
    Dog('Шарик', 10, 'Доберман'),
    Cat('Матроскин', 9, True),
]
for animal in animals:
    animal.make_voice()
