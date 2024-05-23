# solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"

import pytest
from snoop import snoop
from typing import Any

def solution(args: list[int]):
    pass            

def check_list_in_order(l: list[int]) -> Any:
    """Recursive check for whether the elements in the provided  list are in order."""
    if len(l) == 1:
        return True
    if l[1] == l[0] + 1:
        return check_list_in_order(l[1:])
    else:
        return False
    

@pytest.mark.parametrize("input, expected", 
    [
        ([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20], '-6,-3-1,3-5,7-11,14,15,17-20'),
        ([-3,-2,-1,2,10,15,16,18,19,20], '-3--1,2,10,15,16,18-20'),
    ],
    ids=["input1", "input2"]
)
def test_solution(input, expected):
    assert solution(input) == expected
