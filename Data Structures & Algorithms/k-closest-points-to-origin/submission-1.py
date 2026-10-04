class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #caluculating the distances 
        minHeap = []
        for point in points:
            x, y = point[0], point[1]
            distance = math.sqrt(x**2 + y**2)
            heapq.heappush(minHeap, (distance, [x,y]))
        
        res = []
        for count in range(k):
            dist, point = heapq.heappop(minHeap)
            res.append(point)
        return res