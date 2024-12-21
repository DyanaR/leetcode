# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # two pointers, one for each list to compare them 
        # head of each list
        dummy = ListNode()
        cur = dummy
        
        while list1 and list2:
            # compare nodes to assign new head
            if list1.val < list2.val or list1.val == list2.val: #if list 1 has smaller node than make that one head
                cur.next = list1
                cur = list1
                list1 = list1.next
            elif list2.val < list1.val:
                cur.next = list2
                cur = list2
                list2 = list2.next
        
        cur.next = list1 if list1 else list2
        return dummy.next