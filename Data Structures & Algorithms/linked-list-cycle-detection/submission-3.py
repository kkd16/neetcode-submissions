# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head is None:
            return False

        slow_curr = head
        fast_curr = head

        while fast_curr and fast_curr.next:

            slow_curr = slow_curr.next
            fast_curr = fast_curr.next.next

            if fast_curr == slow_curr:
                return True

            
        return False
        