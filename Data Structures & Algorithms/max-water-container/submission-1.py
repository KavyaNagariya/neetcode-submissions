class Solution:
    def maxArea(self, heights: List[int]) -> int:
        st, end = 0, len(heights)-1
        maxArea = 0
        while st < end:
            width = end - st
            high = min(heights[end], heights[st])
            maxArea = max(maxArea, width*high)
            if heights[st] <= heights[end]:
                st += 1
                continue
            end -= 1
        return maxArea