class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root):

        result = []

        def inorder(node):

            if node is None:
                return

            # Left
            inorder(node.left)

            # Root
            result.append(node.val)

            # Right
            inorder(node.right)

        inorder(root)

        return result


# Create Tree
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

# Run
solution = Solution()

print(solution.inorderTraversal(root))



# Leetcode Problem 94: Binary Tree Inorder Traversal

# class Solution:
#     def inorderTraversal(self, root):

#         result = []

#         def inorder(node):

#             if node is None:
#                 return

#             # Left
#             inorder(node.left)

#             # Root
#             result.append(node.val)

#             # Right
#             inorder(node.right)

#         inorder(root)

#         return result
