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
            level = []
            n = len(q)
            for _ in range(n):
                curr = q.popleft()
                level.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            res.append(level[-1])

        return res

        