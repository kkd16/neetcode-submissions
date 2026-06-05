class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        cols = defaultdict(set)

        chunks = defaultdict(set)

        for row in range(9):
            for col in range(9):                  
                n = board[row][col]

                if n == '.':
                    continue

                chunk = (row // 3, col // 3)

                if n in rows[row] or n in cols[col] or n in chunks[chunk]:
                    return False

                rows[row].add(n)
                cols[col].add(n)
                chunks[chunk].add(n)


        return True
