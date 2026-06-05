class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        cols = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        # 3 * (row // 3) + (col // 3)

        for id_row, row in enumerate(board):
            for id_col, val in enumerate(row):

                if val == ".":
                    continue

                sq = 3 * (id_row // 3) + (id_col // 3)

                if val in rows[id_row] or val in cols[id_col] or val in squares[sq]:
                    return False

                
                rows[id_row].add(val)
                cols[id_col].add(val)
                squares[sq].add(val)
 
        return True