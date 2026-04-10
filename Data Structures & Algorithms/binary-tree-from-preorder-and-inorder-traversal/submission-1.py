# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

       
        def build_level(preorder, inorder):

            if not preorder or not inorder:
                return None

            root = preorder[0]
            root_idx = inorder.index(root)

            return TreeNode(
                root,
                build_level(preorder[1:], inorder[0:root_idx]),
                build_level(preorder[1 + root_idx:], inorder[1 + root_idx:])
            )

        return build_level(preorder, inorder)
      