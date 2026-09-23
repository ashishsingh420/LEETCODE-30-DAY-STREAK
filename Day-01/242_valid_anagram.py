s = "anagram"
t = "nagaram"

if len(s) != len(t):
    print(False)
else:
    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1

    for char in t:
        if char not in count:
            print(False)
            break

        count[char] -= 1

        if count[char] < 0:
            print(False)
            break
    else:
        print(True)




#Leetcode Problem 242: Valid Anagram

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:

#         if len(s) != len(t):
#             return False

#         count = {}

#         for char in s:
#             count[char] = count.get(char, 0) + 1

#         for char in t:
#             if char not in count:
#                 return False

#             count[char] -= 1

#             if count[char] < 0:
#                 return False

#         return True