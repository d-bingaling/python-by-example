# Test for ex35
import pytest


def shape_one(side_length):
    area = side_length * side_length
    return area


def shape_two(base, height):
    area = (base * height) / 2
    return area


@pytest.mark.parametrize("side_length, expected", [(9, 81), (10, 100)])
def test_shape_one(side_length, expected):
    assert shape_one(side_length) == expected


@pytest.mark.parametrize("base, height, expected", [(10, 20, 100), (7, 3, 10.5)])
def test_shape_two(base, height, expected):
    assert shape_two(base, height) == expected
