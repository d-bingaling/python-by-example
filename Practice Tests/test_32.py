# test
import pytest
import math


def radi(radius, depth):
    area = math.pi * (radius ** 2)
    volume = round(area * depth, 3)
    return volume


@pytest.mark.parametrize(
    "radius, depth, expected", [(6, 7, 791.681), (11, 13, 4941.725)]
)
def test_radi(radius, depth, expected):
    assert radi(radius, depth) == expected
