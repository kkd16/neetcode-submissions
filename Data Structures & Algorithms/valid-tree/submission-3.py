class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 != len(edges):
            return False

        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for nei in adj[node]:
                dfs(nei)

        dfs(0)

        return len(visited) == n
        