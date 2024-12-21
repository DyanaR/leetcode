# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None

        while cur: # while curr is not null
            temp = cur.next # temp var to not lose list
            cur.next = prev # curr node points at prev node we created
            prev = cur
            cur = temp
        
        return prev