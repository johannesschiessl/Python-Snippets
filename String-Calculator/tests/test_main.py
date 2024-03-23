import pytest

import sys
sys.path.append('../')

from src.main import add

@pytest.mark.parametrize(
    "input, expected",
    [
        ("", "0"),
        ("1", "1"),
        ("22,2", "24"),
        ("11,13,10", "34"),
        ("1\n2,3", "6"),
        ("175,\n35", "Number expected but '\n' found"),
        ("1,3,", "Number expected but EOF found.")
    ]
)

def test_add(input, expected):
    assert add(input) == expected