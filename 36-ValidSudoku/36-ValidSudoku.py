# Last updated: 8/22/2025, 11:37:11 AM
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    # U: check t or f if each col, row, sq are sets
    # M: hash set, integer divison
    # P: traverse through every square, adding it to row, col, sq set
    # use int division to break into squares 
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        # [key(r/c, c/3) = which square it is in: val set]
        sqs = collections.defaultdict(set)
        for r in range(len(board)): 
            rowSet = set()
            for c in range(9):
                # check for empty
                if board[r][c] == ".":
                    continue
                # check for duplicate 
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or
                    board[r][c] in sqs[(r // 3, c // 3)]):
                        return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                sqs[(r // 3, c // 3)].add(board[r][c])
        # sqs = {(0, 0): {'8', '9', '4', '2', '1'}, (0, 1): {'3', '5'}, (0, 2): {'3'}...etc
        return True

        
    # indx of each square - (row / 3) * 3 + (col / 3)

    # Time Complexity: O(n^2) where n is rows in the grid aka 9
    # Space Complexity: O(n^2)