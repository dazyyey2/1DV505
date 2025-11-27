import pytest
from my_fractions import Fraction


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


def test_subtraction():
    f1 = Fraction(1, 2)
    f2 = Fraction(2, 4)
    expected = Fraction(0, 1)
    assert str(f1-f2) == str(expected), f'Exp: {str(expected)},Got: {
        str(f1-f2)}'
    f1 = Fraction(1, 3)
    f2 = Fraction(2, 4)
    expected = Fraction(-1, 6)
    assert str(f1-f2) == str(expected), f'Exp: {str(expected)}, Got: {
        str(f1-f2)}'
    f1 = Fraction(1, 8)
    f2 = Fraction(2, 8)
    expected = Fraction(-1, 8)
    assert str(f1-f2) == str(expected), f'Exp: {str(expected)}, Got: {
        str(f1-f2)}'
    f1 = Fraction(100, 200)
    f2 = Fraction(200, 400)
    expected = Fraction(0, 1)
    assert str(f1-f2) == str(expected), f'Exp: {str(expected)}, Got: {
        str(f1-f2)}'
    f1 = Fraction(300, 200)
    f2 = Fraction(200, 400)
    expected = Fraction(1, 1)
    assert str(f1-f2) == str(expected), f'Exp: {str(expected)}, Got: {
        str(f1-f2)}'


def test_multiplication():
    f1 = Fraction(1, 2)
    f2 = Fraction(2, 4)
    expected = Fraction(1, 4)
    assert str(f1*f2) == str(expected), f'Exp: {str(expected)},Got: {
        str(f1*f2)}'
    f1 = Fraction(1, 3)
    f2 = Fraction(2, 4)
    expected = Fraction(1, 6)
    assert str(f1*f2) == str(expected), f'Exp: {str(expected)}, Got: {
        str(f1*f2)}'
    f1 = Fraction(1, 8)
    f2 = Fraction(2, 8)
    expected = Fraction(1, 32)
    assert str(f1*f2) == str(expected), f'Exp: {str(expected)}, Got: {
        str(f1*f2)}'
    f1 = Fraction(100, 200)
    f2 = Fraction(200, 400)
    expected = Fraction(1, 4)
    assert str(f1*f2) == str(expected), f'Exp: {str(expected)}, Got: {
        str(f1*f2)}'
    f1 = Fraction(300, 200)
    f2 = Fraction(200, 400)
    expected = Fraction(3, 4)
    assert str(f1*f2) == str(expected), f'Exp: {str(expected)}, Got: {
        str(f1*f2)}'


def test_division():
    f1 = Fraction(1, 2)
    f2 = Fraction(2, 4)
    expected = Fraction(1, 1)
    assert str(f1/f2) == str(expected), f'Exp: {str(expected)},Got: {
        str(f1/f2)}'
    f1 = Fraction(1, 3)
    f2 = Fraction(2, 4)
    expected = Fraction(2, 3)
    assert str(f1/f2) == str(expected), f'Exp: {str(expected)}, Got: {
        str(f1/f2)}'
    f1 = Fraction(1, 8)
    f2 = Fraction(2, 8)
    expected = Fraction(1, 2)
    assert str(f1/f2) == str(expected), f'Exp: {str(expected)}, Got: {
        str(f1/f2)}'
    f1 = Fraction(100, 200)
    f2 = Fraction(200, 400)
    expected = Fraction(1, 1)
    assert str(f1/f2) == str(expected), f'Exp: {str(expected)}, Got: {
        str(f1/f2)}'
    f1 = Fraction(300, 200)
    f2 = Fraction(200, 400)
    expected = Fraction(3, 1)
    assert str(f1/f2) == str(expected), f'Exp: {str(expected)}, Got: {
        str(f1/f2)}'


def test_div_by_zero():
    with pytest.raises(ValueError) as exc_info:
        Fraction(2, 0)
    expected_message = 'Denominator in a fraction cannot be 0.'
    result_message = str(exc_info.value)
    assert result_message == expected_message, 'Expected error message'
    f'{expected_message}, but got {result_message}'
