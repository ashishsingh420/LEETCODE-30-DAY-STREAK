nums = [1, 2, 3, 1]

if len(nums) != len(set(nums)):
    print(True)
else:
    print(False)




# Leetcode Problem 217: Contains Duplicate

# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:

#         return len(nums) != len(set(nums))