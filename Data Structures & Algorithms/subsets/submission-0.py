class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        #T: O(n * 2^n)
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            #decision to take nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            #decision to not take nums[i]
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res


