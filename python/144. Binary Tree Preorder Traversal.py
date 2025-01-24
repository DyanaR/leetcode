# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        # base case
        def traverse(node):

            if not node:
                return

            result.append(node.val)

            # go through all of left side
            traverse(node.left)
            # go through all of right side
            traverse(node.right)

        traverse(root)
        return result

# TIME COMPLEXITY:  O(n)
# SPACE COMPLEXITY: O(n)