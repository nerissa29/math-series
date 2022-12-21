import pytest
# from package_name.module_name import function_name
from series.series import fibonacci
from series.series import lucas

# pytest tests must start with "test_"


"""
Below is the test run for function lucas()
"""
def test_fibonacci_exists():
    assert fibonacci


def test_fibonacci_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_fibonacci_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_fibonacci_other():
    actual = fibonacci(-2)
    expected = "Please enter numbers >= 0"
    assert actual == expected


def test_fibonacci_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fibonacci_eight():
    actual = fibonacci(8)
    expected = 21
    assert actual == expected

"""
Below is the test run for function lucas()
"""

def test_lucas_exists():
    assert lucas


def test_lucas_zero():
    actual = lucas(0)
    expected = 2
    assert actual == expected


def test_lucas_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_lucas_two():
    actual = lucas(3)
    expected = 4
    assert actual == expected


def test_lucas_seven():
    actual = lucas(7)
    expected = 29
    assert actual == expected


