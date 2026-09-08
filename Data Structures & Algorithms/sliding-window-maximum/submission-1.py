class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #Brute forced solution
        '''left, right = 0, k - 1
        maxElements = [] 
        while right < len(nums):
            largest = nums[left] 
            for i in range(left, right + 1):
                largest  = max(largest, nums[i])
            maxElements.append(largest)
            right += 1
            left += 1
        return maxElements'''

        #Solution using the deque
        output = []
        q = collections.deque() # storing indices of the largest noticeble values
        l = r = 0
        while r < len(nums):
            #pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            #remove the left val from window 
            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        
        return output