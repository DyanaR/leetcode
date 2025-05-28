# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # similar to Maximum Depth of Binary Tree Problem
        # recursively - preorder DFS

        # function to calc height 
        def height(node):
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)
            return 1 + max(left, right)
        
        if not root:
            return True

        left_height = height(root.left)
        right_height = height(root.right)

        if abs(left_height - right_height) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

        # TIME COMPLEXITY: O(n^2)