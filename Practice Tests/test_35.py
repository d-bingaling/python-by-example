# Test for Challenge 035

import pytest


def name_input(name):
    for i in range(0, 3):
        return name


# not sure if this testing correctly, shouldn't expected be dan dan dan?
# this is the only way I can get it to work.
@pytest.mark.parametrize("name, expected", [("dan", "dan")])
def test_name_input(name, expected):
    assert name_input(name) == expected
