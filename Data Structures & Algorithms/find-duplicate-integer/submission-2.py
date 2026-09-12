class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Solution with the slow and fast pointers and floyds algorithm do check solution once
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow or slow2
