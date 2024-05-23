"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""

def remove_duplicates(nums: list[int]) -> int:
    """Solution for non-dec order with two-pointer approach"""
    left = 1
    for right in range(1, len(nums)):
        if nums[right] != nums[right-1]:
            nums[left] = nums[right]
            left += 1
    return left
    
input_arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
c = remove_duplicates(input_arr)
print(input_arr, c)
