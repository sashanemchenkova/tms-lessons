import math


class Rational:
    def __init__(self, nominator, denominator):
        self.__nominator = nominator
        self.__denominator = denominator
        self.__normalise()

    @property
    def nominator(self):
        return self.__nominator

    @property
    def denominator(self):
        return self.__denominator

    def __str__(self):
        return f'{self.nominator}/{self.denominator}'

    def __mul__(self, number: 'Rational') -> 'Rational':
        return Rational(self.nominator * number.nominator, self.denominator * number.denominator)

    def __truediv__(self, number: 'Rational') -> 'Rational':
        return Rational(self.nominator * number.denominator, self.denominator * number.nominator)

    # return self * Rational(number.d, number.n)

    def __add__(self, number: 'Rational') -> 'Rational':
        new_nominator = self.nominator * number.denominator + self.denominator * number.nominator
        new_denominator = self.denominator * number.denominator
        return Rational(new_nominator, new_denominator)

    def __sub__(self, number: 'Rational') -> 'Rational':
        new_nominator = self.nominator * number.denominator - self.denominator * number.nominator
        new_denominator = self.denominator * number.denominator
        return Rational(new_nominator, new_denominator)

    # self + Rational(-numder.n, number.d)

    def __eq__(self, number: "Rational"):
        return self.nominator == number.nominator, self.denominator == number.denominator

    # n1*d2 = n2*d1

    def __ne__(self, number: "Rational"):
        return self.nominator != number.nominator or self.denominator != number.denominator

    # return not(self == number)

    def __lt__(self, number: "Rational"):
        if self.nominator == number.nominator:
            return self.denominator > number.denominator  # self.n/self.d < other.n/other.d
        else:
            return self.nominator < number.nominator

    def __le__(self, number: "Rational"):
        if self.nominator == number.nominator:
            return self.denominator >= number.denominator
        else:
            return self.nominator <= number.nominator

    def __gt__(self, number: "Rational"):
        if self.nominator == number.nominator:
            return self.denominator < number.denominator
        else:
            return self.nominator > number.nominator

    def __ge__(self, number: "Rational"):
        if self.nominator == number.nominator:
            return self.denominator <= number.denominator
        else:
            return self.nominator >= number.nominator

    def __normalise(self):
        gcd = math.gcd(self.nominator, self.denominator)
        self.__nominator //= gcd
        self.__denominator //= gcd
        if self.denominator < 0:
            self.__denominator *= -1
            self.__nominator *= -1


if __name__ == '__main__':
    my_number = Rational(1, 2)
    assert my_number.nominator == 1
    assert my_number.denominator == 2
    # print(my_number)
    num = Rational(1, 3)
    # print(my_number.__mul__(num))
    # print(my_number.__truediv__(num))
    # print(my_number.__add__(num))
    print(my_number.__sub__(num))
    print(num.__sub__(my_number))
    # assert Rational(1, 2) == Rational(1, 2)
    assert Rational(1, 2) != Rational(1, 3)
    assert Rational(1, 3) < Rational(1, 2)
    assert Rational(1, 3) < Rational(2, 3)
    assert Rational(1, 3) <= Rational(1, 2)
    assert Rational(5, 2) > Rational(1, 2)
    assert Rational(5, 2) >= Rational(5, 2)
    assert Rational(1, 2) >= Rational(1, 3)
    result = Rational(1, 4) * (Rational(3, 2) + Rational(1, 8)) + Rational(156, 100)
    print(result)
    assert Rational(3, 2) + Rational(1, 8) == Rational(26, 16)
    assert Rational(13, 8) * Rational(1, 4) == Rational(13, 32)
    assert Rational(13, 32) + Rational(156, 100) == Rational(6292, 3200)
    print(Rational(2, 4))
    assert Rational(2, 4) == '1 / 2'
