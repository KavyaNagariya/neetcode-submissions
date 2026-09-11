# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #Dumb solution but my solution works on paper but not on test cases
        '''
        firstNum = secondNum = 0
        multiplier = 10
        curr = l1
        # first get the firstNum
        while curr:
            if curr == l1:
                firstNum += l1.val
            else:
                firstNum += curr.val * multiplier
                multiplier *= 10
            curr = curr.next
        
        multiplier = 10
        curr = l2
        # second get the secondNum
        while curr:
            if curr == l2:
                secondNum += l2.val
            else:
                secondNum += curr.val * multiplier
                multiplier *= 10
            curr = curr.next
        # store the sums digits in the list 
        Sum = firstNum + secondNum
        resList = []
        while Sum > 0:
            digit = Sum % 10
            resList.append(digit)
            Sum //= 10
        resHead = ListNode(resList[0]) if resList[0] else ListNode()
        curr = resHead
        # create new linked list while traversing the list from behind
        for val in resList[1:]:
            valNode = ListNode(val)
            curr.next = valNode
            curr = curr.next
        return resHead
        '''
        # Correct Solution
        dummy = ListNode()
        curr = dummy

        carry = 0
        while l1 or l2 or carry: # we want to carry on if the l1 and l2 are like 8 and 4  which means sum is 12
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit 
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)

            # updating the pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
