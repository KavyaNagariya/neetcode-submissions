class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        # Counter for the min heap just negative the values and then heapify the array it would work as a max Heap just when you pop the value multiply it with -1
        heapq.heapify(maxHeap)
        
        while len(maxHeap) > 1:
            first = heapq.heappop(maxHeap)
            second = heapq.heappop(maxHeap)
            if second > first:
                heapq.heappush(maxHeap, first - second)
        if len(maxHeap) == 0:
            return 0
        return abs(maxHeap[0])
            

