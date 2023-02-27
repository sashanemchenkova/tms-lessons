from person import Person

my_friends = [
    Person('Petr Petrov', 25, 'M'),
    Person('Maria Ivanova', 12, 'F'),
    Person('Ivan Sokolov', 19, 'M')

]
for person in my_friends:
    person.print_person_info()