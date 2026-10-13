class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        # solution that saves space by not using set for path 

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (r < 0 or c < 0 
                or r >= ROWS or c >= COLS 
                or word[i] != board[r][c]):
                return False

            temp = board[r][c]
            board[r][c] = "#" # mark as visited 

            res = (dfs(r + 1, c , i + 1) or 
                    dfs(r - 1, c, i + 1) or 
                    dfs(r, c + 1, i + 1) or 
                    dfs(r, c - 1, i + 1))
            board[r][c] = temp #Using this to clean if the dfs return false 
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True
            
        return False
        #T: O(n * m * 4^k) k: len(word)