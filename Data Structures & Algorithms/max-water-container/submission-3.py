class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        st, end = 0, len(heights)-1
        while st < end:
            h = min(heights[st], heights[end])
            w = end - st
            maxArea = max(h*w, maxArea)
            if heights[st] <= heights[end]:
                st += 1
                continue
            end -= 1

        return maxArea
            