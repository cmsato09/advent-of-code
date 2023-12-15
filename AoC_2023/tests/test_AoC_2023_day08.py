import pytest

import AoC_2023.solutions.AoC_2023_day08 as day08

@pytest.mark.parametrize('dir, curr_node, next', [
    ('R', ('BBB', 'CCC'), 'CCC'),
    ('L', ('ZZZ', 'GGG'), 'ZZZ'),
])
def test_step_direction(dir, curr_node, next):
    assert day08.step_direction(dir, curr_node) == next


@pytest.mark.parametrize('directions, test_network, total_steps', [
    ('LLR', 
    {'AAA': ('BBB', 'BBB'),
     'BBB': ('AAA', 'ZZZ'),
     'ZZZ': ('ZZZ', 'ZZZ')}, 
     6),
])
def test_reach_end(directions, test_network, total_steps):
    assert day08.reach_end(directions, test_network) == total_steps