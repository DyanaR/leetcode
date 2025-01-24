# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # perform DFS preorder
        # we are countinng number of nodes in each branch to 
        # find the max depth
        # therefore each node should account for the value of 1
        # if there is no node the value is 0
        # hence the base case below
        if not root:
            return 0

        # start be checking left side and left subtrees first
        left = self.maxDepth(root.left)
        # now check the right side and right subtrees
        right = self.maxDepth(root.right)

        return 1 + max(left, right)