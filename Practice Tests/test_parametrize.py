import pytest

# pytest Tests/test_parametrize.py::test_add

# test add


def add(x, y):
    return x + y


@pytest.mark.parametrize(
    "x,y,expected", [(3, 5, 8), ("Hello", " World", "Hello World"), (5.5, 6.5, 12)]
)
def test_add(x, y, expected):
    assert add(x, y) == expected


# test multiply


def mult(x, y):
    return x * y


@pytest.mark.parametrize("x,y,expected", [(2, 10, 20), (5, 5, 25), (8.0, 8.0, 64.0)])
def test_mult(x, y, expected):
    assert mult(x, y) == expected


# test divide


def div(a, b):
    return a / b


@pytest.mark.parametrize("a,b, expected", [(10, 2, 5), (15, 5, 3), (95, 2, 47.5)])
def test_div(a, b, expected):
    assert div(a, b) == expected
