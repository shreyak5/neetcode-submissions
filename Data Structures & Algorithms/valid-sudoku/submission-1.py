class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        # row check
        for r in range(9):
            check = [0]*9
            for c in range(9):
                if board[r][c] == '.':
                    continue
                num = int(board[r][c]) - 1
                if check[num] == 1:
                    return False
                check[num] = 1

        # column check
        for c in range(9):
            check = [0]*9
            for r in range(9):
                if board[r][c] == '.':
                    continue
                num = int(board[r][c]) - 1
                if check[num] == 1:
                    return False
                check[num] = 1

        # grid check
        for g in range(9):
            r_beg = 3*(g//3)
            c_beg = 3*(g%3)
            check = [0]*9
            for r in range(r_beg, r_beg + 3):
                for c in range(c_beg, c_beg + 3):
                    if board[r][c] == '.':
                        continue
                    num = int(board[r][c]) - 1
                    if check[num] == 1:
                        print(g, r_beg, c_beg, r, c)
                        return False
                    check[num] = 1

        return True

        