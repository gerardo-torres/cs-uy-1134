def move_zeroes(nums):
"""
: nums type: list[int]
: return type: void
"""
for i in range(len(nums)):
    if nums[i] == 0:
        nums.append(nums.pop(i))

move_zeroes([1, 0, 0, 0, 13, 0, 0, 0, 43])
