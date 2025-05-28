# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # DFS - PREORDER
        # if both trees are empty or reached node leaves
        # then theyre the same
        if not p and not q:
            return True
        # if both nodes exist and values match
        if p and q and p.val == q.val:
            # recursively check nodes
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        return False