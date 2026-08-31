class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left, right = 0, m*n - 1 # matrix: m*n
        while left <= right:
            mid = left + ((right - left) // 2)
            midVal = matrix[mid // n][mid % n]
            if target == midVal:
                return True
            elif target > midVal:
                left = mid + 1
            else:
                right = mid - 1
        return False    