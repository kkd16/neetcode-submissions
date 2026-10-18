# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return 0

        def dfs(curr, m):
            if not curr:
                return 0
            
            res = 1 if curr.val >= m else 0

            m = max(m, curr.val)

            res += dfs(curr.left, m)
            res += dfs(curr.right, m)
            return res

        return  dfs(root, root.val)
