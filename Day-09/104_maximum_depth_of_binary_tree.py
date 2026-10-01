# Leetcode Problem 104: Maximum Depth of Binary Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root):

        if root is None:
            return 0

        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        return 1 + max(leftDepth, rightDepth)


# Create Tree
root = TreeNode(3)

root.left = TreeNode(9)

root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


# Run
solution = Solution()

print(solution.maxDepth(root))


# Leetcode Problem 104: Maximum Depth of Binary Tree

# class Solution:
#     def maxDepth(self, root):

#         if root is None:
#             return 0

#         leftDepth = self.maxDepth(root.left)
#         rightDepth = self.maxDepth(root.right)

#         return 1 + max(leftDepth, rightDepth)