# Test for Challenge 035
import pytest

from hypothesis import given, strategies as st
from challenges.exercises.ex35 import display_input_three_times


@pytest.mark.parametrize("name, length, expected", [("dan", 3, ["dan", "dan", "dan"])])
def test_name_input(name, length, expected):
    result = display_input_three_times(name)
    assert result == expected
    assert len(result) == length
