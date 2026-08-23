class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(height[l], leftMax)
                if leftMax - height[l] > 0:
                    res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(height[r], rightMax)
                if rightMax - height[r] > 0:
                    res += rightMax - height[r]
        return res
        