class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Trivial Solution : Create a hashmap and keep checking the count and then return the key if the count > 1
        countMap = defaultdict()
        for num in nums:
            if num in countMap:
                return num
            else:
                countMap[num] = 1