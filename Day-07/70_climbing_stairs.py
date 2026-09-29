n = 5

if n <= 2:
    print(n)
else:

    first = 1
    second = 2

    for i in range(3, n + 1):

        third = first + second

        first = second
        second = third

    print(second)


# Leetcode Problem 70: Climbing Stairs

# class Solution:
#     def climbStairs(self, n: int) -> int:

#         if n <= 2:
#             return n

#         first = 1
#         second = 2

#         for i in range(3, n + 1):

#             third = first + second

#             first = second
#             second = third

#         return second