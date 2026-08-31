class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        st, end = 1, max(piles)
        res = end
        while st <= end:
            mid = (end + st) // 2
            hour = 0
            for p in piles:
                hour += math.ceil(p / mid)
             
            if hour <= h:
                res = min(res, mid)
                end = mid - 1
            else:
                st = mid + 1
        return res

                

