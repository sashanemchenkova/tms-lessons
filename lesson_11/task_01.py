# Создайте класс MyTime с одним полем seconds (типа float).

class MyTime:
    def __init__(self, seconds):
        self.seconds: float = float(seconds)
        # Добавьте методы-свойства (@property) hours и minutes, которые возвращают int (целое количество часов и
        # минут соответственно).

    @property
    def hours(self) -> int:
        return int(self.seconds) // 3600

    @property
    def minutes(self) -> int:
        return int(self.seconds) % 3600 // 60

    # Переопределите магические методы умножения и деления на число. Пример: MyTime(5) * 2 будет равно MyTime(10).

    def __mul__(self, other: float) -> 'MyTime':
        return MyTime(self.seconds * other)

    def __truediv__(self, other: float) -> 'MyTime':
        return MyTime(self.seconds / other)

    def __floordiv__(self, other: float) -> 'MyTime':
        return MyTime(self.seconds // other)

    def __eq__(self, other: 'MyTime') -> bool:
        return self.seconds == other.seconds

    def __add__(self, other: 'MyTime') -> 'MyTime':
        return MyTime(self.seconds + other.seconds)

    def __sub__(self, other: 'MyTime') -> 'MyTime':
        return MyTime(self.seconds - other.seconds)

    def get_formatted_str(self):
        seconds_from_min_start = self.seconds % 60

        return f'{self.hours: 02d }:{self.minutes: 02d}:{seconds_from_min_start: 04.1f}.'

    def __str__(self):
        return f'{self.seconds}s'

# class MyTimeInterval:
#     def __init__(self, start_seconds, end_seconds):
#         MyTime.start = start_seconds
#         MyTime.finish = end_seconds
#
#     def is_inside(self, other : 'MyTime') -> bool:

    def __ne__(self, other: 'MyTime') -> bool:
        return self.seconds != other.seconds

    def __lt__(self, other: 'MyTime') -> bool:
        return self.seconds < other.seconds

    def __gt__(self, other: 'MyTime') -> bool:
        return self.seconds > other.seconds

    def __le__(self, other: 'MyTime') -> bool:
        return self.seconds <= other.seconds

    def __ge__(self, other: 'MyTime') -> bool:
        return self.seconds >= other.seconds





if __name__ == '__main__':
    time = MyTime(3724.5)
    assert time.hours == 1
    print(time.hours)
    assert time.minutes
    print(time.minutes)
    assert MyTime(5) * 2 == MyTime(10)
    assert MyTime(5) / 2 == MyTime(2.5)
    assert MyTime(5) // 2 == MyTime(2)
    assert MyTime(5) + MyTime(2) == MyTime(7)
    assert MyTime(5) - MyTime(2) == MyTime(3)
    print(MyTime(10))
    assert str(MyTime(10)) == '10.s'

