from collections import deque

class Solution:



    def numIslands(self, grid: List[List[str]]) -> int:

        seen = set()

        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c):

            q = deque()
            q.append((r, c))

            while q:
                (r, c) = q.popleft()

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (nr in range(rows) and
                        nc in range(cols) and
                        grid[nr][nc] == '1' and
                        (nr, nc) not in seen):
                            q.append((nr, nc))
                            seen.add((nr, nc))  

        islands = 0

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in seen and grid[r][c] == '1':
                    islands += 1
                    bfs(r, c)

                    
        return islands