# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        prev, curr = None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        newHead = prev
        curr = newHead
        prev = None
        while n > 0:
            n -= 1
            prev = curr
            curr = curr.next
        
        if n == 0:
            prev = curr.next
            curr.next = None
        
        againPrev, againCurr = None, newHead
        while againCurr:
            next = againCurr.next
            againCurr.next = againPrev
            againPrev = againCurr
            againCurr = next
        return againPrev
        '''

        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next 

