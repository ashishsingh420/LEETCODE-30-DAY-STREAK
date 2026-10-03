class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def diameterOfBinaryTree(self, root):

        diameter = 0

        def height(node):

            nonlocal diameter

            if node is None:
                return 0

            leftHeight = height(node.left)
            rightHeight = height(node.right)

            diameter = max(diameter, leftHeight + rightHeight)

            return 1 + max(leftHeight, rightHeight)

        height(root)

        return diameter


# Create Tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


# Run
solution = Solution()

print(solution.diameterOfBinaryTree(root))


# class Solution:
#     def diameterOfBinaryTree(self, root):

#         diameter = 0

#         def height(node):

#             nonlocal diameter

#             if node is None:
#                 return 0

#             leftHeight = height(node.left)
#             rightHeight = height(node.right)

#             diameter = max(diameter, leftHeight + rightHeight)

#             return 1 + max(leftHeight, rightHeight)

#         height(root)

#         return diameter