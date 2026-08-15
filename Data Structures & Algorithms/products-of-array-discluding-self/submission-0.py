class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        for i in range(1,len(nums)):
            #prefix sums in results
            ans[i] = nums[i-1] * ans[i-1]


        suffix = 1
        for i in range(len(nums)-2,-1,-1):
            #suffix
            suffix *= nums[i+1]
            ans[i] *= suffix
        return ans



