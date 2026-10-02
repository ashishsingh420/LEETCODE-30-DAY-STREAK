class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSameTree(self, p, q):

        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


    def isSubtree(self, root, subRoot):

        if subRoot is None:
            return True

        if root is None:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


# Create Root Tree

root = TreeNode(3)

root.left = TreeNode(4)
root.right = TreeNode(5)

root.left.left = TreeNode(1)
root.left.right = TreeNode(2)


# Create SubRoot Tree

subRoot = TreeNode(4)

subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)


# Check

solution = Solution()

print(solution.isSubtree(root, subRoot))



# Leetcode Problem 572: Subtree of Another Tree

# class Solution:

#     def isSameTree(self, p, q):

#         if p is None and q is None:
#             return True

#         if p is None or q is None:
#             return False

#         if p.val != q.val:
#             return False

#         return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


#     def isSubtree(self, root, subRoot):

#         if subRoot is None:
#             return True

#         if root is None:
#             return False

#         if self.isSameTree(root, subRoot):
#             return True

#         return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)