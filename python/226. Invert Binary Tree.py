# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # since range of nodes are [0, 100] using recursion will be fine

        # case if theres no node 
        if not root:
            return 

        # swap child nodes
        root.left, root.right = root.right, root.left

        self.invertTree(root.left) # processes entire left tree before moving to right
        self.invertTree(root.right)

        return root

