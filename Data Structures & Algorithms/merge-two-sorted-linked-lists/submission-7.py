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

        currRes = head

        while curr1 and curr2:
            if curr1.val < curr2.val:
                currRes.next = curr1
                curr1 = curr1.next

            else:
                currRes.next = curr2
                curr2 = curr2.next

            currRes = currRes.next

        while curr1:
            currRes.next = curr1
            curr1 = curr1.next
            currRes = currRes.next
        
        while curr2:
            currRes.next = curr2
            curr2 = curr2.next
            currRes = currRes.next

        return head.next

        
        