import pytest

# Test for exersice 45


def ex_fortyfive(num):
    total = 0
    while total <= 50:
        total = total + num
        return total


@pytest.mark.parametrize("num, expected", [(2, 2), (3, 3)])
def test_ex_fortyfive(num, expected):
    assert ex_fortyfive(num) == expected
