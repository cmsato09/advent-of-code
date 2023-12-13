import pytest
from AoC_2023.solutions.AoC_2023_day01 import findFirstandLast

@pytest.mark.parametrize('input_string, expected_result', [
    ('1abc2', 12),
    ('pqr3stu8vwx', 38),
    ('a1b2c3d4e5f', 15),
    ('treb7uchet', 77),
])
def test_findFirstandLast(input_string, expected_result):
    assert findFirstandLast(input_string) == expected_result
