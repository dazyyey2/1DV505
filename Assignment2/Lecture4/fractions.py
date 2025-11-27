class Fraction:
    def __init__(self, numerator, denominator):
        if denominator != 0:
            if denominator < 0:
                # If denominator is negative, flip so that
                # numerator is negative instead
                self.__numerator = numerator * -1
                self.__denominator = denominator * -1
            else:
                self.__numerator = numerator
                self.__denominator = denominator
        else:
            raise ValueError('Denominator in a fraction cannot be 0.')

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

    def simplified(self):
        gcd = 1  # Start at 1 because every number can be divided by 1
        k = 2
        # Find greatest common divisor
        while k <= self.__numerator and k <= self.__denominator:
            if self.__numerator % k == 0 and self.__denominator % k == 0:
                gcd = k
            k += 1
        # Should be okay to do integer devision because we
        # know the result won't be a float
        new_numerator = self.__numerator // gcd
        new_denominator = self.__denominator // gcd
        return Fraction(new_numerator, new_denominator)

    # Addition
    def __add__(self, f2):
        if self.denominator == f2.denominator:
            return Fraction(self.numerator + f2.numerator,
                            self.denominator).simplified()
        else:
            return Fraction((self.numerator * f2.denominator) +
                            (f2.numerator * self.denominator),
                            (self.denominator * f2.denominator)).simplified()

    # Subtraction
    def __sub__(self, f2):
        if self.denominator == f2.denominator:
            return Fraction(self.numerator - f2.numerator,
                            self.denominator).simplified()
        else:
            return Fraction((self.numerator * f2.denominator) -
                            (f2.numerator * self.denominator),
                            (self.denominator * f2.denominator)).simplified()

    # Multiplication
    def __mul__(self, f2):
        return Fraction(self.numerator * f2.numerator,
                        self.denominator * f2.denominator).simplified()

    # Float division
    def __truediv__(self, f2):
        return Fraction(self.numerator * f2.denominator,
                        self.denominator * f2.numerator).simplified()

    def __str__(self):
        return f'{self.__numerator}/{self.__denominator}'


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
