# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []


        q = collections.deque([root])
        res = []
        while q:
            n = len(q)
            for i in range(n):
                c = q.popleft()
                if c.left:
                    q.append(c.left)
                if c.right:
                    q.append(c.right)
                right = c.val

                if i == n - 1:
                    res.append(c.val)

        return res

        

        