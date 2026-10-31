class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # loop thru entire grid
        # when u hit an island start dfs on it
        # set cells to 0 when u hit and store max

        # store current search area
        # store max seen overall

        rows = len(grid)
        cols = len(grid[0])

        res = 0
        curr = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            if grid[r][c] == 1:
                nonlocal curr
                nonlocal res
                curr += 1
                res = max(res, curr)
                grid[r][c] = 0

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue

                    dfs(nr, nc)
            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    curr = 0
                    dfs(r, c)

        return res

            