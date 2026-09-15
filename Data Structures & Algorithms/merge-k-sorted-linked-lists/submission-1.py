# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #Working code but TLE T: O(k*n)
        '''
        if not lists:
            return None

        p1 = lists[0]
        for i in range(1, len(lists)):
            p1 = self.merge(p1, lists[i])
        return p1
    
    def merge(self, head1, head2):
        dummy = ListNode(0)
        curr = dummy

        p1, p2 = head1, head2
        while p1 and p2:
            if p1.val <= p2.val:
                curr.next = p1
                p1 = p1.next
            else:
                curr.next = p2
                p2 = p2.next
            curr = curr.next
        
        if p1:
            curr.next = p1
        else:
            curr.next = p2
        return dummy.next
        '''

        # Optimized Solution using merge sort kind of so T: O(logk * n)
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergeList = []

            for i in range(0, len(lists), 2):
                p1 = lists[i]
                p2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergeList.append(self.merge(p1, p2))
            lists = mergeList
        return lists[0]
    
    def merge(self, head1, head2):
        dummy = ListNode(0)
        curr = dummy

        p1, p2 = head1, head2
        while p1 and p2:
            if p1.val <= p2.val:
                curr.next = p1
                p1 = p1.next
            else:
                curr.next = p2
                p2 = p2.next
            curr = curr.next
        
        if p1:
            curr.next = p1
        else:
            curr.next = p2
        return dummy.next

        