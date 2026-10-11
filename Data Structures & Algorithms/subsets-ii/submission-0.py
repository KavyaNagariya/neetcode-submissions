class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # Including the nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            #Not including the nums[i]
            # The next iteration where we are not including the nums[i] should not contain the same value as of nums[i] so we will skip the duplicate values
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res