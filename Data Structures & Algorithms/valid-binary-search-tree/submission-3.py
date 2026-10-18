# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True

        def dfs(node, cmax, cmin):
            if not node:
                return True

            if node.val >= cmax or node.val <= cmin:
                return False

            return dfs(node.left, node.val, cmin) and dfs(node.right, cmax, node.val)

        return dfs(root, float('inf'), float('-inf'))
        