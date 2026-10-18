# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        q = deque()
        q.append(root)

        res = []
        while q:
            level = []
            n = len(q)
            for _ in range(n):
                curr = q.popleft()
                level.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                
                if curr.right:
                    q.append(curr.right)

            res.append(level)

        return res


        