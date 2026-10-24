class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        isVisited = {}
        for i, n in enumerate(nums):
            diff = target - n 
            if diff in isVisited:
                return [isVisited[diff], i]
            isVisited[n] = i