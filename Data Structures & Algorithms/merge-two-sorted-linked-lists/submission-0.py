# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        curr1 = list1 
        curr2 = list2

        head = ListNode()

        curr_out = head

        while curr1 and curr2:

            if curr1.val < curr2.val:
                curr_out.next = curr1
                curr1 = curr1.next
            
            else:
                curr_out.next = curr2
                curr2 = curr2.next

            curr_out = curr_out.next

        while curr1:
            curr_out.next = curr1
            curr1 = curr1.next
            curr_out = curr_out.next

        while curr2:
            curr_out.next = curr2
            curr2 = curr2.next
            curr_out = curr_out.next

        return head.next
