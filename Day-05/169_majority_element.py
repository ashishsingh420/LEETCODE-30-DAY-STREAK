nums = [2, 2, 1, 1, 1, 2, 2]

candidate = nums[0]
count = 1

for i in range(1, len(nums)):

    if nums[i] == candidate:
        count += 1
    else:
        count -= 1

    if count == 0:
        candidate = nums[i]
        count = 1

print(candidate)



# Leetcode Problem 169: Majority Element

# class Solution:
#     def majorityElement(self, nums: list[int]) -> int:

#         candidate = nums[0]
#         count = 1

#         for i in range(1, len(nums)):

#             if nums[i] == candidate:
#                 count += 1
#             else:
#                 count -= 1

#             if count == 0:
#                 candidate = nums[i]
#                 count = 1

#         return candidate