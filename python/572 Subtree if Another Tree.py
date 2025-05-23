# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if not p and not q: 
                return True
            if p and q and p.val == q.val:
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
            
        if not root:
            return False # if theres no root then there cant be a subroot
        if isSameTree(root, subRoot): # if this returns true then its same 
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) 

