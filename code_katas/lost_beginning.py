"""
Given a sequence of one or more consecutive natural numbers concatenated into a string, return the smallest possible first number in the sequence.
Numbers will never be truncated.

"123" -> [1, 2, 3] -> 1
"1234567891" -> [1234567891] -> 1234567891
"91011" -> [9, 10, 11] -> 9
"17181920" -> [17, 18, 19, 20] -> 17
"9899100" -> [98, 99, 100] -> 98
"121122123" -> [121, 122, 123] -> 121
"1235" -> [1235] -> 1235
"101" -> [101] -> 101
"""

from snoop import snoop

def split_nums_to_list(nums: str, group_size: int):
    if "9"*group_size not in nums:
        num_list = [int(nums[i:i+group_size]) for i in range(0, len(nums), group_size)]
    else:
        ...
    return num_list

def check_nums_consecutive(nums: list):
    for i in range(len(nums) - 1):
        if nums[i+1] != nums[i] + 1:
            return False
    return True

@snoop
def solution(input_str: str):
    group_size = 1
    while 2*group_size <= len(input_str):
        if int(input_str[0:group_size]) + 1 == int(input_str[group_size:2*group_size]):
            if check_nums_consecutive(split_nums_to_list(input_str, group_size)):
                return split_nums_to_list(input_str, group_size)[0]
        group_size += 1
    return int(input_str)

             
