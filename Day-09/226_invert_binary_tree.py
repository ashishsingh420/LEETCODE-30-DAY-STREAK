# Leetcode Problem 226: Invert Binary Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root):

        if root is None:
            return None

        # Swap left and right
        root.left, root.right = root.right, root.left

        # Invert left subtree
        self.invertTree(root.left)

        # Invert right subtree
        self.invertTree(root.right)

        return root


# Create Tree

root = TreeNode(4)

root.left = TreeNode(2)
root.right = TreeNode(7)

root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

root.right.left = TreeNode(6)
root.right.right = TreeNode(9)


# Invert Tree

solution = Solution()
solution.invertTree(root)


# Print Inorder to check result

def inorder(node):

    if node is None:
        return

    inorder(node.left)
    print(node.val, end=" ")
    inorder(node.right)


inorder(root)


# Leetcode Problem 226: Invert Binary Tree

# class Solution:
#     def invertTree(self, root: TreeNode | None) -> TreeNode | None:
#         if root is None:
#             return None

#         # Swap left and right
#         root.left, root.right = root.right, root.left

#         # Invert left subtree
#         self.invertTree(root.left)

#         # Invert right subtree
#         self.invertTree(root.right)

#         return root