class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #create a maxheap takes O(nlogn)
        maxHeap = []
        for val in nums:
            heapq.heappush(maxHeap, -val)
        
        # Iterate over the maxHeap till Kth largest element
        res = 0
        while k > 0:
            res = -heapq.heappop(maxHeap)
            k -= 1
        return res
