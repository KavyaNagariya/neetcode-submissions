class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        st, end = 0, len(numbers)-1
        while st < end:
            sum = numbers[st] + numbers[end]
            if sum == target:
                return [st+1, end+1]
            elif sum < target:
                st += 1
            else:
                end -= 1