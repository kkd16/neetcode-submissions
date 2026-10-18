# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        res = True
        def dfs(curr):
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)

            nonlocal res
            if left > right + 1:
                res = False

            if right > left + 1:
                res = False

            return max(left, right) + 1

        dfs(root)
        return res

    
        