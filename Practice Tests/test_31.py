# test
import pytest
import math


def radi(radius):
    area = math.pi * (radius ** 2)
    return area


@pytest.mark.parametrize(
    "radius, expected", [(10, 314.1592653589793), (12, 452.3893421169302)]
)
def test_radi(radius, expected):
    assert radi(radius) == expected
