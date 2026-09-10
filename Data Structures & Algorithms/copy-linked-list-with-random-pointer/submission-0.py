"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        copyMap = { None: None }

        while curr:
            copy = Node(curr.val)
            copyMap[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = copyMap[curr]
            copy.next = copyMap[curr.next] #if curr.next or curr.random is Null then fixed using the None: None in the copyMap so that if it finds the None it will get None 
            copy.random = copyMap[curr.random]
            curr = curr.next

        return copyMap[head]
