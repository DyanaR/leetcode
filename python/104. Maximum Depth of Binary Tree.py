# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # post order DFS - RECURSIVE
        # if not root:
        #     return 0

        # left = self.maxDepth(root.left)
        # right = self.maxDepth(root.right)

        # return 1 + max(left, right)

        # TIME COMPLEXITY: O(n)
        # SPACE COMPLEXITY: O(h) - h: height of the tree
            # worst case: O(n)
            # best case: O(log n)

        # BFS - ITERATIVE - FIFO
        # if not root:
        #     return 0
        
        # level = 0 
        # queue = [root]
        # while queue:
        #     for i in range(len(queue)): # for the current nodes in the queue at each level
        #         node = queue.pop(0)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     level += 1
        # return level

        # TIME COMPLEXITY: O(n)
        # SPACE COMPLEXITY: O(h) - h: height of the tree
            # worst case: O(n) - bottom level has many nodes

        # DFS - ITERATIVE 
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
        return res

        # TIME COMPLEXITY: O(n)
        # SPACE COMPLEXITY: O(w) - w: width of the tree
            # worst case: O(n)
            # best case: O(log n)



