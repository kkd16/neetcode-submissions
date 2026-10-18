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

        res = False
        def dfs(curr):
            if not curr:
                return
            nonlocal res
            if sameTree(curr, subRoot):
                res = True

            left = dfs(curr.left)
            right = dfs(curr.right)

            if left or right:
                res = True
            

        dfs(root)
        return res

        