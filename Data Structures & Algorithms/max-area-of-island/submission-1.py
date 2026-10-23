class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        islands = 0
        maxArea = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))
            area = 1

            while q:
                trow , tcol = q.popleft()
                directions =  [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    row, col = trow + dr, tcol + dc
                    if (row in range(rows) and col in range(cols)
                         and (row, col) not in visit
                        and grid[row][col] == 1):
                        area += 1
                        visit.add((row, col))
                        q.append((row, col))
            return area
                

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    maxArea = max(maxArea, bfs(r, c))
                    islands += 1

        return maxArea