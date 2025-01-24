# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # inorder traversal:  visit the left child first, then the node, and finally the right child
        result = []
        def traverse(node):
            if not node:
                return

            #base case
            traverse(node.left)
            result.append(node.val)
            traverse(node.right)
        
        traverse(root)
        return result
    
# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)