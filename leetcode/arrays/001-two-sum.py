"""
https://leetcode.com/problems/two-sum/description/

Given an array of integers `nums` and an integer `target`, return indices of the two numbers
such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the
same element twice.

You can return the answer in any order.
"""
def two_sum(nums: list[int], target: int) -> list[int]:
    num_map = {}  # num:index
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in num_map:
            return [num_map[complement], i]
        num_map[nums[i]] = i
        

if __name__ == "__main__":
    input = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6),
    ]
    expected = [
        [0, 1],
        [1, 2],
        [0, 1]
    ]
    i = 0
    for nums, target in input:
        assert two_sum(nums, target) == expected[i], f"{two_sum(nums, target)} != {expected[i]}"
        i += 1
    print("All tests passed!")
