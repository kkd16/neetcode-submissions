# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
       
        count = 0

        def dfs(curr, m):
            nonlocal count

            if not curr:
                return

            if curr.val >= m:
                count += 1

            dfs(curr.left, max(m, curr.val))
            dfs(curr.right, max(m, curr.val))
        
        if root:
            dfs(root, root.val)
        
        return count