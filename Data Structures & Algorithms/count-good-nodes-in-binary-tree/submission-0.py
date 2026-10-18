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
        
        m = root.val
        self.count = 0

        def dfs(curr, m):
            if not curr:
                return
            if curr.val >= m:
                self.count += 1

            m = max(m, curr.val)

            dfs(curr.left, m)
            dfs(curr.right, m)

        dfs(root, m)

        return self.count