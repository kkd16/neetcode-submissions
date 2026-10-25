# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        count = k
        res = root.val

        def dfs(curr):
            nonlocal count, res
            if not curr or count == 0:
                return

            dfs(curr.left)

            if count == 0:
                return
            
            count -= 1
            if count == 0:
                res = curr.val
                return

            dfs(curr.right)

        dfs(root)
        return res


