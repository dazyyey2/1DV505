class Fraction:
    def __init__(self, numerator, denominator):
        if denominator != 0:
            if denominator < 0:
                # If denominator is negative, flip so that
                # numerator is negative instead
                self.numerator = numerator * -1
                self.denominator = denominator * -1
            else:
                self.numerator = numerator
                self.denominator = denominator
        else:
            raise ValueError('Denominator in a fraction cannot be 0.')
        # Simplify fraction
        gcd = 1  # Start at 1 because every number can be divided by 1
        k = 2
        # Find greatest common divisor
        # FAILED test_fraction.py::test_subtraction
        # - AssertionError: Exp: -1/6, Got: -2/12
        # Fixed with absolute values
        while k <= abs(self.numerator) and k <= abs(self.denominator):
            if self.numerator % k == 0 and self.denominator % k == 0:
                gcd = k
            k += 1
        # Should be okay to do integer devision because we
        # know the result won't be a float
        self.numerator //= gcd
        self.denominator //= gcd

    @property
    def numerator(self):
        return self.__numerator

    @numerator.setter
    def numerator(self, numerator):
        self.__numerator = numerator

    @property
    def denominator(self):
        return self.__denominator

    @denominator.setter
    def denominator(self, denominator):
        self.__denominator = denominator

    # Addition
    def __add__(self, f2):
        if self.denominator == f2.denominator:
            return Fraction(self.numerator + f2.numerator,
                            self.denominator)
        else:
            return Fraction((self.numerator * f2.denominator) +
                            (f2.numerator * self.denominator),
                            (self.denominator * f2.denominator))

    # Subtraction
    def __sub__(self, f2):
        if self.denominator == f2.denominator:
            return Fraction(self.numerator - f2.numerator,
                            self.denominator)
        else:
            return Fraction((self.numerator * f2.denominator) -
                            (f2.numerator * self.denominator),
                            (self.denominator * f2.denominator))

    # Multiplication
    def __mul__(self, f2):
        return Fraction(self.numerator * f2.numerator,
                        self.denominator * f2.denominator)

    # Float division (flip f2 denominator and numerator)
    def __truediv__(self, f2):
        return Fraction(self.numerator * f2.denominator,
                        self.denominator * f2.numerator)

    def __str__(self):
        # FAILED test_fraction.py::test_subtraction
        # - AssertionError: Exp: 0,Got: 0/8
        if self.numerator != 0:
            return f'{self.numerator}/{self.denominator}'
        else:
            return '0'


# Prevent running program by importing
if __name__ == '__main__':
    f1 = Fraction(3, 4)
    f2 = Fraction(2, 5)
    print(f"f1: {f1}")
    print(f"f2: {f2}")
    print("\nCalculations:")
    print(f"f1 + f2 = {f1 + f2}")
    print(f"f1 - f2 = {f1 - f2}")
    print(f"f1 * f2 = {f1 * f2}")
    print(f"f1 / f2 = {f1 / f2}")
