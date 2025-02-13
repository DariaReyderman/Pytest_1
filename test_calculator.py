import time
from unittest import expectedFailure
from webbrowser import Error

# testable

import pytest
from pyexpat import ExpatError

import calculator


def test_calculator_add_small():
    # Arrange
    a: int = 2
    b: int = 5
    expected: int = 7

    # Act
    actual: int = calculator.add(a, b)

    # Assert
    assert expected == actual, "small numbers add"


# pip install pytest
# option 1 - run the tests: play
# option 2 - run the tests in the Terminal: pytest
# add test sub
# add test mul
# add test div

def test_calculator_minus_small():
    # Arrange
    a: int = 10
    b: int = 10
    expected: int = 0

    # Act
    actual: int = calculator.minus(a, b)

    # Assert
    assert expected == actual, "small numbers minus"


def test_calculator_multiply_small():
    # Arrange
    a: int = 10
    b: float = 0.1
    expected: float = 1.0

    # Act
    actual: int = calculator.multiply(a, b)

    # Assert
    assert expected == actual, "small numbers multiply"


def test_calculator_div_small():
    # Arrange
    a: int = 10
    b: float = 0.1
    expected: float = 100

    # Act
    actual: int = calculator.divide(a, b)

    # Assert
    assert expected == actual, "small numbers div"


# False positive
def test_calculator_div_by_zero1():
    # Arrange
    a: int = 10
    b: float = 0

    # Act
    try:
        # next line should raise an error
        calculator.divide(a, b)

        # if we got here it's incorrect
        # the test should fail!
        # since we expected ZeroDivisionError to occur
        assert False, "should raise ZeroDivisionError"
    except ZeroDivisionError as e:
        # this is a good scenario
        # an error has occurred
        # test should pass successfully
        assert True


def test_calculator_div_by_zero2():
    # Arrange
    a: int = 10
    b: float = 0

    # Act
    # this means
    # if ZeroDivisionError will happen
    #       test will pass successfully
    #       if not - test will fail
    with pytest.raises(Exception) as ex:
        calculator.divide(a, b)


def test_check_error_happened():
    with pytest.raises(IndexError) as ex:
        calculator.make_error()


# sending input value to a functions during test
# extra feature, *bonus
def test_calculator_hello(monkeypatch):
    # black box
    monkeypatch.setattr('builtins.input', lambda _: "danny1")

    expected = "hello danny"
    result = calculator.say_hello()

    assert expected == result


# ------- HOMEWORK -------
# d
def test_calculator_power_d():
    a: int = 2
    b: int = 4
    expected: int = 16

    actual: int = calculator.power(a, b)

    assert expected == actual, "power of numbers"


# e
def test_calculator_power_e():
    a: int = 3
    b: int = 2
    expected: int = 9

    actual: int = calculator.power(a, b)

    assert expected == actual, "power of numbers"


# f
def test_calculator_sqrt_f():
    b: int = 25
    expected: int = 5

    actual: int = calculator.sqrt(b)

    assert expected == actual, "square root"


# g
def test_calculator_sqrt_g():
    b: int = -5

    with pytest.raises(ValueError) as e:
        calculator.sqrt(b)


# h
def test_calculator_factorial_h():
    c: int = 4
    expected: int = 24

    actual: int = calculator.factorial(c)

    assert expected == actual, "factorial of a number"


# i
def test_calculator_factorial_i():
    c: int = 5
    expected: int = 120

    actual: int = calculator.factorial(c)

    assert expected == actual, "factorial of a number"


# j
def test_calculator_factorial_j():
    c: int = -3
    with pytest.raises(ValueError):
        calculator.factorial(c)
