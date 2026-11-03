class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROW, COL = defaultdict(set), defaultdict(set) #Set for each row and column in where they have occured like for row 2 : (1,2,3,4) are the values 
        square = defaultdict(set) # for assuming that no value in the square should come if thats already in a square (that would violate the sudoku rule), key = ( r // 3, c // 3)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in ROW[r] or 
                    board[r][c] in COL[c] or 
                    board[r][c] in square[(r // 3, c // 3)]):
                    return False
                ROW[r].add(board[r][c]) 
                COL[c].add(board[r][c]) 
                square[(r // 3, c // 3)].add(board[r][c])
        return True # T: O(r * c)