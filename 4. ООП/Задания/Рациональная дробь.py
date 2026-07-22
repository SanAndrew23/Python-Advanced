class Rational:
    def __init__(self, a, b):
        self.numerator = a
        self.denominator = b
        self.reduce()

    def reduce(self):
        def gcd(a, b):
            while b > 0:
                a, b = b, a % b
            return a

        g = gcd(self.numerator, self.denominator)
        self.numerator = self.numerator // g
        self.denominator = self.denominator // g

    def __add__(self, other):
        return Rational(self.numerator * other.denominator + self.denominator * other.numerator,
                        self.denominator * other.denominator)

    def __sub__(self, other):
        return Rational(self.numerator * other.denominator - self.denominator * other.numerator,
                        self.denominator * other.denominator)

    def __mul__(self, other):
        return Rational(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        return Rational(self.numerator * other.denominator, self.denominator * other.numerator)

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def __lt__(self, other):
        return self.numerator * other.denominator < self.denominator * other.numerator

    def __gt__(self, other):
        return other < self

    def __le__(self, other):
        return not (other < self)

    def __ge__(self, other):
        return not (other > self)

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __ne__(self, other):
        return not (self == other)

    def __float__(self):
        return self.numerator / self.denominator


dr1 = Rational(4, 5)
dr2 = Rational(1, 5)
print(dr1 + dr2)
print(dr1 - dr2)
print(dr1 * dr2)
print(dr1 / dr2)
print(dr1 < dr2)
print(dr1 > dr2)
print(dr1 <= dr2)
print(dr1 >= dr2)
print(dr1 == dr2)
print(dr1 != dr2)
print(float(dr1))
