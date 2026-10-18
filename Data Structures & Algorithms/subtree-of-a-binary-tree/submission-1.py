# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(a, b):
            if not a and not b:
                return True

            if not a or not b:
                return False

            if a.val != b.val:
                return False

            return sameTree(a.left, b.left) and sameTree(a.right, b.right)


        if sameTree(root, subRoot):
            return True

        if not root:
            return False

        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        if left or right:
            return True

        return False

        