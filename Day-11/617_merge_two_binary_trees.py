class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def mergeTrees(self, root1, root2):

        if root1 is None:
            return root2

        if root2 is None:
            return root1

        root1.val = root1.val + root2.val

        root1.left = self.mergeTrees(root1.left, root2.left)

        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1


# Tree 1
root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)


# Tree 2
root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(7)


# Run
solution = Solution()

mergedRoot = solution.mergeTrees(root1, root2)


# Print Preorder
def preorder(node):

    if node is None:
        return

    print(node.val, end=" ")

    preorder(node.left)
    preorder(node.right)


preorder(mergedRoot)


# class Solution:
#     def mergeTrees(self, root1, root2):

#         if root1 is None:
#             return root2

#         if root2 is None:
#             return root1

#         root1.val = root1.val + root2.val

#         root1.left = self.mergeTrees(root1.left, root2.left)

#         root1.right = self.mergeTrees(root1.right, root2.right)

#         return root1