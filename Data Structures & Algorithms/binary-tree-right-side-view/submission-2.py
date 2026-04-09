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
    
        q = collections.deque()

        q.append(root)

        level_order = []

        res = []

        while q:
            level_len = len(q)
            level = []
            for i in range(level_len):

                node = q.popleft()

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

                level.append(node.val)

                if i == level_len - 1:
                    res.append(node.val)

            level_order.append(level)
        

        return res

        

        