"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""

def remove_duplicates(nums: list[int]) -> int:
    """Solution for non-dec order with two-pointer approach"""
    uniq = 1
    for curr in range(1, len(nums)):
        if nums[curr] != nums[curr-1]:
            nums[uniq] = nums[curr]
            uniq += 1
    return uniq
    
input_arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
c = remove_duplicates(input_arr)
print(input_arr, c)
