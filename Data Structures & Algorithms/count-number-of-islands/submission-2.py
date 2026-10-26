class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        count = 0

        def bfs(sr, sc):
            q = collections.deque()
            q.append((sr, sc))
            grid[i][j] == "0"

            while q:
                (r, c) = q.popleft()
                for (dr, dc) in directions:
                    nr = r + dr
                    nc = c + dc

                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols:
                        if grid[nr][nc] == "1":
                            q.append((nr, nc))
                            grid[nr][nc] = "0"



        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count += 1
                    bfs(i, j)

        return count         

        