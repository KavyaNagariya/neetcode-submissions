class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        least = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                least = min(nums[l], least)
                break
            m = (r + l) // 2
            least = min(least, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return least