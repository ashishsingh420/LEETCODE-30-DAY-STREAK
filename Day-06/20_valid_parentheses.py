s = "([])"

stack = []

pairs = {
    ')': '(',
    ']': '[',
    '}': '{'
}

for char in s:

    if char in pairs:

        if not stack or stack[-1] != pairs[char]:
            print(False)
            break

        stack.pop()

    else:
        stack.append(char)

else:
    print(len(stack) == 0)



# Leetcode Problem 20: Valid Parentheses

# class Solution:
#     def isValid(self, s: str) -> bool:

#         stack = []

#         pairs = {
#             ')': '(',
#             ']': '[',
#             '}': '{'
#         }

#         for char in s:

#             if char in pairs:
#                 if not stack or stack[-1] != pairs[char]:
#                     return False

#                 stack.pop()

#             else:
#                 stack.append(char)

#         return len(stack) == 0