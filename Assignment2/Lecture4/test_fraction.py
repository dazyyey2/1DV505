import pytest
from fractions import Fraction


def test_addition():
    f1 = Fraction(1, 2)
    f2 = Fraction(2, 4)
    expected = Fraction(1, 1)
    assert str(f1+f2) == str(expected), f'Exp: {str(expected)},Got: {
        str(f1+f2)}'
    f1 = Fraction(1, 3)  # 4/12
    f2 = Fraction(2, 4)  # 6/12
    expected = Fraction(5, 6)
    assert str(f1+f2) == str(expected), f'Exp: {str(expected)}, Got: {
        str(f1+f2)}'
    f1 = Fraction(1, 8)
    f2 = Fraction(2, 8)
    expected = Fraction(3, 8)
    assert str(f1+f2) == str(expected), f'Exp: {str(expected)}, Got: {
        str(f1+f2)}'
    f1 = Fraction(100, 200)
    f2 = Fraction(200, 400)
    expected = Fraction(1, 1)
    assert str(f1+f2) == str(expected), f'Exp: {str(expected)}, Got: {
        str(f1+f2)}'
    return
