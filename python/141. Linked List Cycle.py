# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visitedNodes = set()
        cur = head
        while cur:
            if cur in visitedNodes:
                return True
            visitedNodes.add(cur)
            cur = cur.next
        return False