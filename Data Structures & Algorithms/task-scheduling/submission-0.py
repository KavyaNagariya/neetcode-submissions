class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #hashMap = {}
        #for val in tasks:
        #    hashMap[val] = hashMap.get(val, 0) + 1
        #or just use a Counter(tasks)

        #each task 1 unit time 
        #minimize idle time 
        # T: O(n * m) - where n = least n CPU cycles between identical tasks, m = no. of tasks, since n is very less so we can just make T: O(n) and the S:O(n)
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque() #pair of values [-cnt, idleTime]

        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt != 0:
                    q.append([cnt, time + n])
                
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time