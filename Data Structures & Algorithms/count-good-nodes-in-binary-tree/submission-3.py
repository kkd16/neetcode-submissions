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
        
        count = 0

        def dfs(curr, m):

            if not curr:
                return
            nonlocal count
            if curr.val >= m:
                count += 1

            m = max(m, curr.val)

            dfs(curr.left, m)
            dfs(curr.right, m)

        dfs(root, root.val)

        return count