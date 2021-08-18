from typing import Type
import pytest

from hypothesis import given, strategies as st
from tuples_lists_dicts.exercise.ex71 import display_sorted_sports


@pytest.mark.parametrize(
    "fave_sport, expected",
    [
        ("Cricket", ["Badminton", "Cricket", "Gymnastics", "Handball", "Volleyball"]),
        ("Dancing", ["Badminton", "Dancing", "Gymnastics", "Handball", "Volleyball"]),
        ("Hockey", ["Badminton", "Gymnastics", "Handball", "Hockey", "Volleyball"]),
    ],
)
def test_sorted_list_output(fave_sport, expected):
    assert display_sorted_sports(fave_sport) == expected


@pytest.mark.parametrize(
    "fave_sport, error",
    [
        ("cricket", TypeError),
        ("golf", TypeError),
        ("HOCKEY", TypeError),
    ],
)
def test_for_no_caps(fave_sport, error):
    with pytest.raises(error):
        display_sorted_sports(fave_sport)


# setting a default value of 'String', seeing if it gets added to the list
@given(st.just(value="String"))
def test_list_items(fave_sport):
    assert display_sorted_sports(fave_sport)
