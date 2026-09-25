nums = [2, 2, 1]

answer = 0

for num in nums:
    answer = answer ^ num

print(answer)



# Leetcode Problem 136: Single Number

# class Solution:
#     def singleNumber(self, nums: list[int]) -> int:

#         answer = 0

#         for num in nums:
#             answer = answer ^ num

#         return answer