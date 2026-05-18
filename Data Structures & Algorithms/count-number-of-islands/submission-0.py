from collections import deque

class Solution:

    def bfs(self, grid: List[List[str]], seen, si, sj):

        q = deque()
        q.append((si, sj))

        while q:
            (i, j) = q.popleft()

            if i > 0 and seen[i - 1][j] == 0 and grid[i - 1][j] == '1':
                q.append((i - 1, j))
                seen[i - 1][j] = 1
            
            if j > 0 and seen[i][j - 1] == 0 and grid[i][j - 1] == '1':
                q.append((i, j - 1))
                seen[i][j - 1] = 1

            if i < len(grid) - 1 and seen[i + 1][j] == 0 and grid[i + 1][j] == '1':
                q.append((i + 1, j))
                seen[i + 1][j] = 1

            if j < len(grid[0]) - 1 and seen[i][j + 1] == 0 and grid[i][j + 1] == '1':
                q.append((i, j + 1))
                seen[i][j + 1] = 1


        





    def numIslands(self, grid: List[List[str]]) -> int:

        seen = [[0 for _ in row] for row in grid]

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if seen[i][j] != 1 and grid[i][j] == '1':
                    count += 1
                    self.bfs(grid, seen, i, j)

                    


        return count