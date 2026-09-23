s = "A man, a plan, a canal: Panama"

clean = ""

for char in s:
    if char.isalnum():
        clean += char.lower()

if clean == clean[::-1]:
    print(True)
else:
    print(False)





#Leetcode Problem 125: Valid Palindrome

# class Solution:
#     def isPalindrome(self, s: str) -> bool:

#         clean = ""

#         for char in s:
#             if char.isalnum():
#                 clean += char.lower()

#         return clean == clean[::-1]