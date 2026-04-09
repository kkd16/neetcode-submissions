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

            level_order.append(level)
        
        print(level_order)

        res = []

        for level in level_order:
            res.append(level[-1])

        return res

        

        