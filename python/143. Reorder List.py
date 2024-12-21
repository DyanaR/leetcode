# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # to find middle part of list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next # increments by one
            fast = fast.next.next # increment by two
        
        second = slow.next # second part of list starts here

        # introduce a Null to seperate lists
        prev = None
        slow.next = None

        # reverse Next pointers of 2nd part
        while second: # as long as second is not null
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # manipulate nodes in correct order
        one, two = head, prev
        while two:
            temp1, temp2 = one.next, two.next
            one.next = two
            two.next = temp1
            one, two = temp1, temp2