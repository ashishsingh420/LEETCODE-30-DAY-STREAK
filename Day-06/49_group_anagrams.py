strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = {}

for word in strs:

    key = ''.join(sorted(word))

    if key not in groups:
        groups[key] = []

    groups[key].append(word)

print(list(groups.values()))


# Leetcode Problem 49: Group Anagrams

# class Solution:
#     def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

#         groups = {}

#         for word in strs:

#             key = ''.join(sorted(word))

#             if key not in groups:
#                 groups[key] = []

#             groups[key].append(word)

#         return list(groups.values())