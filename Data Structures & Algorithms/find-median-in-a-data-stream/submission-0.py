class MedianFinder:

    def __init__(self):
        self.small, self.large = [], [] #small is a maxHeap, large is a minHeap (values in the small(maxHeap) must be smaller than large(minHeap))

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        # make sure every val in small(maxHeap) < = every val in large(minHeap)
        if (self.small and self.large and -1 * self.small[0] > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        #if uneven length
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        #for odd length of datastream
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]

        return (-1 * self.small[0] + self.large[0]) / 2 # for even
        