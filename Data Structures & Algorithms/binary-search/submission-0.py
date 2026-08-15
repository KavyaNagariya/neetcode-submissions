class Solution:
    def search(self, nums: List[int], target: int) -> int:
        st, end = 0, len(nums)-1
        while st <= end:
            mid = st + (end-st)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                st = mid + 1
            else:
                end = mid - 1
        return -1

